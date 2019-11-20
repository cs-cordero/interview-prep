#!/bin/bash

# Tests for code quality
set -e

flake8 . --count
isort -rc -c .
black . --check
