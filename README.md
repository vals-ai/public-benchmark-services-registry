# public-benchmark-services-registry

Public pilot registry for benchmark services that can be shared outside Vals.

This registry intentionally contains only:

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

## Verify public-readiness

```bash
make verify
```

The verification script checks the registry files and both service submodules for references that would
require non-public model, service, or Git access. The service repositories currently depend only on the
public `create-benchmark-service` framework plus public Python packages and public dataset/image sources.

## Publication note

The service submodule URLs use HTTPS and point at public repositories so external users can clone the
registry recursively.
