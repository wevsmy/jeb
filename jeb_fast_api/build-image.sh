#!/bin/bash

set -e

BASE_DIR=$(
  cd "$(dirname "$0")" || exit
  pwd
)
echo $BASE_DIR

IMAGE_NAME="jeb_fast_api"
echo "build docker images"
docker build -f "$BASE_DIR/Dockerfile" -t "$IMAGE_NAME:latest" -t "$IMAGE_NAME:$(date +%Y%m%d%H%M%S)" . --no-cache --rm
