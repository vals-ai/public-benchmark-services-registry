# public-benchmark-services-registry

This repository indexes public benchmark services used by
[Valkyrie](https://github.com/vals-ai/Valkyrie). Each service lives in this
registry as a pinned Git submodule and has a matching entry in `services.yaml`.

Current services:

- `swebench-benchmark-service`
- `terminal-bench-benchmark-service`
- `skillsbench-benchmark-service`

## Repository layout

```text
public-benchmark-services-registry/
├── swebench-benchmark-service/
├── terminal-bench-benchmark-service/
├── skillsbench-benchmark-service/
├── services.yaml
└── Makefile
```

## Setup

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/vals-ai/public-benchmark-services-registry.git
cd public-benchmark-services-registry
```

Or initialize submodules after cloning:

```bash
make install-submodules
```

Submodule URLs use HTTPS and point at public repositories so recursive clones
work without organization-specific SSH access.

## Working locally

See [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md) for setup, test, and smoke-check
commands for running services from this registry on your machine.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Use the
add-service template for new benchmark services and the modify-service template
for updates to an existing service.
