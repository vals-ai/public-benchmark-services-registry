# Contributing

This registry is for public benchmark service definitions that external users
can clone, inspect, and run locally.

## Acceptable contributions

New benchmark services must:

- Be created with, or match the generated structure from,
  [create-benchmark-service](https://github.com/vals-ai/create-benchmark-service).
- Expose the benchmark service API defined by `create-benchmark-service`.
- Use a public Git repository that can be cloned over HTTPS.
- Be added as a Git submodule under `<name>-benchmark-service/`.
- Include a matching `services.yaml` entry with the service key, path,
  repository URL, branch, and public dependencies.
- Pin the submodule to a reviewed commit.
- Provide a root `README.md` with benchmark scope, data requirements, and local
  development commands.
- Provide a root `Dockerfile` for containerized execution.
- Keep all required datasets, nested submodules, model assets, and package
  dependencies publicly accessible or document the public access steps.
- Include a clear license and data-use story for benchmark code and datasets.
- Run locally from a fresh recursive clone.

## Creating a benchmark service

Use `create-benchmark-service` for new service repositories unless there is a
specific reason to preserve an existing implementation.

```bash
uv tool install git+https://github.com/vals-ai/create-benchmark-service.git@main
create-benchmark-service <benchmark-name>
cd <benchmark-name>-benchmark-service
make install
make dev
```

The scaffold creates the expected Python package, `main.py`, `pyproject.toml`,
`Dockerfile`, `Makefile`, README, tests directory, and CI workflow files. Replace
the example implementation with benchmark-specific dataset loading, task setup,
evaluation, and scoring logic before adding the service to this registry.

## Benchmark service API contract

A public benchmark service must subclass `BenchmarkService` and implement these
methods:

| Method | Requirement |
| --- | --- |
| `load_datasets()` | Load each public dataset as `dict[dataset_name, dict[task_id, task_object]]`. |
| `list_tasks(dataset)` | Return public `V1Task` records for `/v1/datasets/{dataset}/tasks`. |
| `retrieve_task(task_id, skip_validation, dataset)` | Return sandbox source, problem path, working directory, timeout, and resource metadata. |
| `setup_task(task_id, sandbox, dataset)` | Prepare the sandbox and stream setup chunks. |
| `evaluate_response(request, dataset)` | Score a text response without a sandbox when the benchmark supports it. Optional if `evaluate_instance` is implemented. |
| `evaluate_instance(task_id, sandbox, dataset)` | Run sandbox-based evaluation and stream result chunks when the benchmark requires a sandbox. |
| `calculate_final_score(evaluation_results, dataset)` | Aggregate per-task results into a final score and metadata. |
| `project_trial_result(result)` | Required only for trial-mode datasets; return the audited fields trial users may see and resubmit for scoring. |

`BenchmarkServiceApp` exposes the service through this API surface:

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Health check. |
| `GET` | `/version` | Framework, service, and service-version metadata. |
| `GET` | `/verify-task-ids` | Validate or filter task IDs, optionally by dataset. |
| `GET` | `/retrieve-task/` | Return task metadata for one task. |
| `WS` | `/ws/setup-task` | Stream sandbox setup progress and result. |
| `POST` | `/evaluate-response/` | Evaluate a plain response without a sandbox. |
| `WS` | `/ws/evaluate-response` | Stream response-only evaluation and retry state. |
| `WS` | `/ws/evaluate-instance` | Stream sandbox evaluation progress and result. |
| `POST` | `/final-score/` | Aggregate internal evaluation results. |
| `GET` | `/v1/datasets/{dataset}/tasks` | Lab-facing public task list. |

Document any benchmark-specific fields returned by `list_tasks`,
`retrieve_task`, `evaluate_response`, `evaluate_instance`, or
`calculate_final_score` in the service README.

Changes to existing services must:

- Keep `.gitmodules`, the submodule commit, and `services.yaml` aligned.
- Preserve recursive HTTPS clone behavior.
- Document any changed setup, dataset, Docker, or runtime requirements.
- Explain behavior changes that affect scoring, task selection, or compatibility
  with existing benchmark runs.
- Include local validation evidence in the pull request.

## Unacceptable contributions

Do not add:

- Private repositories, SSH-only submodule URLs, or private nested submodules.
- Secrets, API keys, access tokens, private credentials, or `.env` files with
  real values.
- Organization-specific cloud account settings, routing settings, or production
  environment files.
- Datasets or artifacts that require non-public access unless the public access
  process is documented and reviewable.
- Generated build outputs, vendored dependency caches, or temporary runtime
  files.
- Services that require unreviewed network calls during tests or local smoke
  checks.
- Changes that make `git clone --recurse-submodules` fail for public users.
- Benchmark behavior changes without corresponding documentation in the service
  README or pull request.

## Required review

All changes to this repository go through pull requests and team review. The
repository ruleset requires an approving code-owner review before changes can be
merged into `main`.
