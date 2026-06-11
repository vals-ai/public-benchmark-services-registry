## New benchmark service

Service name:

Service repository:

Submodule path:

Branch:

## Registry changes

- [ ] Added the service as a Git submodule under `<name>-benchmark-service/`.
- [ ] Added or updated the matching `services.yaml` entry.
- [ ] Pinned the submodule to the reviewed service commit.
- [ ] Confirmed recursive clone works without SSH credentials.

## Service requirements

- [ ] Root `README.md` documents benchmark scope, datasets, and local commands.
- [ ] Root `Dockerfile` builds the service image.
- [ ] Service exposes a health endpoint.
- [ ] Service supports task retrieval.
- [ ] Service supports setup or response evaluation.
- [ ] Service supports instance evaluation when the benchmark requires a sandbox.
- [ ] Service supports final scoring.
- [ ] Public dependencies, datasets, and nested submodules are documented.
- [ ] License and data-use terms are documented.

## Local validation

Commands run:

```bash
make install-submodules
cd <name>-benchmark-service
make install
make test
make docker-build
make docker-run
curl http://localhost:8001/health
```

Result summary:

## Notes for reviewers

Call out any scoring, dataset, task-selection, or compatibility details that need
extra review.
