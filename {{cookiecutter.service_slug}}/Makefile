SHELL := /usr/bin/env bash
PYTHONPATH := src
TMPDIR := $(CURDIR)/.tmp
UV := uv
UV_CACHE_DIR := $(CURDIR)/.uv-cache

export TMPDIR
export UV_CACHE_DIR

.PHONY: \
	bootstrap \
	pre-lint \
	lint \
	post-lint \
	pre-test \
	test \
	post-test \
	pre-build \
	build \
	post-build

bootstrap:
	mkdir -p $(TMPDIR) $(UV_CACHE_DIR)
	$(UV) sync --frozen

pre-lint:

lint:
	mkdir -p $(TMPDIR) $(UV_CACHE_DIR)
	PYTHONPATH=$(PYTHONPATH) $(UV) run --frozen python -m compileall src tests

post-lint:

pre-test:

test:
	mkdir -p $(TMPDIR) $(UV_CACHE_DIR)
	PYTHONPATH=$(PYTHONPATH) $(UV) run --frozen python -m unittest discover -s tests -p 'test_*.py'

post-test:

pre-build:

build:
	mkdir -p $(TMPDIR) $(UV_CACHE_DIR)
	$(UV) build

post-build:
