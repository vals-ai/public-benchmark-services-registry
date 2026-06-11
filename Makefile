.PHONY: install-submodules update-submodules

install-submodules:
	git submodule update --init --recursive -- swebench-benchmark-service terminal-bench-benchmark-service skillsbench-benchmark-service

update-submodules:
	git submodule update --remote -- swebench-benchmark-service terminal-bench-benchmark-service skillsbench-benchmark-service
