#! /usr/bin/env bash

set -e

# BASE_DIR
BASE_DIR=$(
  cd "$(dirname "$0")" || exit
  pwd
)

echo $BASE_DIR

# Let the DB start
sleep 1;
# Run migrations
#alembic upgrade head

echo "hello word"
