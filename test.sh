#!/bin/bash

# Tests for code quality
set -e

flake8 leetcode/ --count
isort -rc -c leetcode/
black leetcode/ --check
