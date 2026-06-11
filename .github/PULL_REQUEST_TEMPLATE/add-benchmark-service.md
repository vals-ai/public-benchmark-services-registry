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

- [ ] Service was generated with, or intentionally matches,
      `create-benchmark-service`.
- [ ] Root `README.md` documents benchmark scope, datasets, and local commands.
- [ ] Root `Dockerfile` builds the service image.
- [ ] `BenchmarkService.load_datasets()` loads every public dataset.
- [ ] `BenchmarkService.list_tasks()` returns public `V1Task` records for
      `/v1/datasets/{dataset}/tasks`.
- [ ] `BenchmarkService.retrieve_task()` returns sandbox source, problem path,
      working directory, timeout, and resource metadata.
- [ ] `BenchmarkService.setup_task()` streams sandbox setup progress and a final
      result.
- [ ] `BenchmarkService.evaluate_response()` supports response-only evaluation
      when applicable.
- [ ] `BenchmarkService.evaluate_instance()` supports sandbox evaluation when
      applicable.
- [ ] `BenchmarkService.calculate_final_score()` aggregates per-task results.
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
