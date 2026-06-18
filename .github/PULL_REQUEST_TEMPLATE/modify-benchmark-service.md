## Benchmark service update

Service name:

Submodule path:

Old service commit:

New service commit:

## Change type

- [ ] Documentation only
- [ ] Dependency update
- [ ] Dataset or task-set update
- [ ] API compatibility update
- [ ] Scoring or evaluation behavior update
- [ ] Docker or local-runtime update

## Registry checks

- [ ] `.gitmodules`, submodule commit, and `services.yaml` remain aligned.
- [ ] Submodule URLs still use HTTPS and public repositories.
- [ ] Local setup instructions are still accurate.
- [ ] The service still exposes the `create-benchmark-service` API expected by
      this registry.
- [ ] Behavior changes are documented in the service README or this PR.

## Compatibility

Describe any effect on existing tasks, datasets, scoring, or historical run
comparability.

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

Call out risky areas, skipped checks, or benchmark-specific review guidance.
