.PHONY: install-submodules update-submodules verify

install-submodules:
	git submodule update --init --recursive -- swebench-benchmark-service terminal-bench-benchmark-service

update-submodules:
	git submodule update --remote -- swebench-benchmark-service terminal-bench-benchmark-service

verify:
	python3 scripts/verify_no_non_public_refs.py
