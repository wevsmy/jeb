#!/usr/bin/env bash

set -e

# BASE_DIR
BASE_DIR=$(
  cd "$(dirname "$0")" || exit
  pwd
)

# cp run

uvicorn app.main:app --reload --host=0.0.0.0 --port 8011
