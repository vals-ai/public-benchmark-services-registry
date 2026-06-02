from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_PATHS = [
    ROOT / "README.md",
    ROOT / "Makefile",
    ROOT / "services.yaml",
    ROOT / ".gitmodules",
    ROOT / "swebench-benchmark-service",
    ROOT / "terminal-bench-benchmark-service",
]
SERVICE_PATHS = [
    ROOT / "swebench-benchmark-service",
    ROOT / "terminal-bench-benchmark-service",
]
SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
}
SKIP_FILES = {Path("scripts/verify_no_non_public_refs.py")}
SKIP_PATH_PARTS = {".github", "workflows"}
SKIP_PATH_PREFIXES = (
    Path("terminal-bench-benchmark-service/datasets"),
)
TEXT_SUFFIXES = {
    "",
    ".dockerfile",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

FORBIDDEN = [
    "git+ssh://",
    "git@github.com:",
    "model-proxy",
    "model_library",
    "prodBenchmarksInfra",
    "benchVals",
    "VALS_API_KEY",
    "DESCOPE_PROJECT_ID",
    "BENCHMARK_API_KEY",
    "s3://",
]

ALLOWED = [
    "create-benchmark-service @ git+https://github.com/vals-ai/create-benchmark-service.git@v0.5.0",
    "uses: vals-ai/.github/.github/workflows/update-lockfile.yaml@main",
]


def iter_files(path: Path):
    if path.is_file():
        yield path
        return

    for child in path.rglob("*"):
        if not child.is_file():
            continue
        rel_path = child.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel_path.parts):
            continue
        if any(part in SKIP_PATH_PARTS for part in rel_path.parts):
            continue
        if any(rel_path.is_relative_to(prefix) for prefix in SKIP_PATH_PREFIXES):
            continue
        if rel_path in SKIP_FILES:
            continue
        if child.suffix.lower() in TEXT_SUFFIXES:
            yield child


def main() -> None:
    findings: list[str] = []
    missing_service_paths = [path.name for path in SERVICE_PATHS if not path.exists()]
    if missing_service_paths:
        print("Skipping absent service submodule contents: " + ", ".join(missing_service_paths))

    for scan_path in SCAN_PATHS:
        if not scan_path.exists():
            continue
        for file_path in iter_files(scan_path):
            try:
                text = file_path.read_text()
            except UnicodeDecodeError:
                continue
            for line_number, line in enumerate(text.splitlines(), start=1):
                if any(allowed in line for allowed in ALLOWED):
                    continue
                for pattern in FORBIDDEN:
                    if pattern.lower() in line.lower():
                        rel_path = file_path.relative_to(ROOT)
                        findings.append(f"{rel_path}:{line_number}: {pattern}")

    if findings:
        raise SystemExit("Non-public references found:\n" + "\n".join(findings))

    print("No non-public service, model, or Git references found.")


if __name__ == "__main__":
    main()
