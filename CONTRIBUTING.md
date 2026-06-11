# Contributing

This registry is for public benchmark service definitions that external users
can clone, inspect, and run locally.

## Acceptable contributions

New benchmark services must:

- Use a public Git repository that can be cloned over HTTPS.
- Be added as a Git submodule under `<name>-benchmark-service/`.
- Include a matching `services.yaml` entry with the service key, path,
  repository URL, branch, and public dependencies.
- Pin the submodule to a reviewed commit.
- Provide a root `README.md` with benchmark scope, data requirements, and local
  development commands.
- Provide a root `Dockerfile` for containerized execution.
- Expose the benchmark service API expected by Vals tooling, including health,
  task retrieval, setup or response evaluation, instance evaluation when
  applicable, and final scoring.
- Keep all required datasets, nested submodules, model assets, and package
  dependencies publicly accessible or document the public access steps.
- Include a clear license and data-use story for benchmark code and datasets.
- Run locally from a fresh recursive clone.

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
