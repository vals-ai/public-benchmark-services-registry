# Local Development

These commands run the registry and its services from a local checkout.

## Prerequisites

- Git with submodule support
- Python 3.12
- `uv`
- Docker, for container builds and benchmark tasks that run in containers

## Clone and install submodules

```bash
git clone --recurse-submodules https://github.com/vals-ai/public-benchmark-services-registry.git
cd public-benchmark-services-registry
```

If you cloned without `--recurse-submodules`, initialize the service submodules:

```bash
make install-submodules
```

Refresh service submodules to their configured upstream branches:

```bash
make update-submodules
```

## Inspect registered services

`services.yaml` lists the public services, their submodule paths, source
repositories, branches, and public dependency notes.

```bash
sed -n '1,200p' services.yaml
git submodule status --recursive
```

## Run SWE-bench locally

```bash
cd swebench-benchmark-service
make install
make setup
make dev
```

The development server prints the selected local port. Open `/docs` on that
port for the FastAPI schema and use `/health` for a basic smoke check.

To run tests:

```bash
make test
```

To build and run the service container:

```bash
make docker-build
make docker-run
curl http://localhost:8001/health
```

## Run Terminal-Bench locally

```bash
cd terminal-bench-benchmark-service
make install-submodules
make install
make dev
```

The development server prints the selected local port. Open `/docs` on that
port for the FastAPI schema and use `/health` for a basic smoke check.

To run tests:

```bash
make test
```

To build and run the service container:

```bash
make docker-build
make docker-run
curl http://localhost:8001/health
```

## Troubleshooting

- If a service says the virtual environment is missing, run `make install` in
  that service directory.
- If a dataset is missing, run the service-specific setup command from its
  README.
- If Docker cannot start benchmark task containers, confirm Docker is running
  and that the task image named by the service can be pulled.
- If recursive clone fails, check that every submodule URL in `.gitmodules` uses
  HTTPS and points to a public repository.
