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

## Create a new benchmark service

New services should start from
[create-benchmark-service](https://github.com/vals-ai/create-benchmark-service)
so they inherit the expected FastAPI app, `BenchmarkService` base class,
schemas, Dockerfile, Makefile, and test layout.

```bash
uv tool install git+https://github.com/vals-ai/create-benchmark-service.git@main
create-benchmark-service <benchmark-name>
cd <benchmark-name>-benchmark-service
make install
make dev
```

The generated service includes a working example. Replace it with your benchmark
implementation, then verify the framework API before adding the service as a
registry submodule:

```bash
make test
make docker-build
make docker-run
curl http://localhost:8001/health
```

The local development server prints its selected port. Use `/docs` on that port
to inspect the generated OpenAPI schema.

## Run a registered service locally

Each service owns its own dataset setup and benchmark-specific commands. Use
this registry to find the service path, then follow that service's README for
any extra setup steps before running it.

Current service paths:

- `swebench-benchmark-service`
- `terminal-bench-benchmark-service`

Generic workflow:

```bash
cd <service-path>
make help
make install
make dev
make test
```

The development server prints its selected local port. Open `/docs` on that port
for the FastAPI schema and use `/health` on that port for a basic smoke check.

For container validation, use the service's Docker targets when present:

```bash
make docker-build
make docker-run
curl http://localhost:8001/health
```

If a service requires dataset downloads, nested submodules, support images, or
other benchmark-specific preparation, keep those instructions in the service
README rather than duplicating them in this registry.

## Troubleshooting

- If a service says the virtual environment is missing, run `make install` in
  that service directory.
- If a dataset is missing, run the service-specific setup command from its
  README.
- If Docker cannot start benchmark task containers, confirm Docker is running
  and that the task image named by the service can be pulled.
- If recursive clone fails, check that every submodule URL in `.gitmodules` uses
  HTTPS and points to a public repository.
