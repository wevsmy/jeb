#!/bin/bash

set -e

BASE_DIR=$(
  cd "$(dirname "$0")" || exit
  pwd
)
echo $BASE_DIR

echo "rm old build h5"
rm -rf "$BASE_DIR/app/h5"
echo "cp new build h5"
cp -r "$BASE_DIR/../jeb_uni_app/unpackage/dist/build/h5" "$BASE_DIR/app"
echo "cp done"
sleep 1