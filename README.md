# public-benchmark-services-registry

A registry of public benchmark services used by [Valkyrie](https://github.com/vals-ai/Valkyrie).

This registry contains:

- `swebench-benchmark-service`
- `terminal-bench-benchmark-service`

Both services are included as HTTPS Git submodules. The registry does not include hosted deployment
infrastructure or customer-specific service configuration.

## Repository layout

```text
public-benchmark-services-registry/
├── swebench-benchmark-service/
├── terminal-bench-benchmark-service/
├── services.yaml
├── Makefile
└── scripts/
```

## Setup

```bash
make install-submodules
```

## Publication note

The service submodule URLs use HTTPS and point at public repositories so external users can clone the
registry recursively.
