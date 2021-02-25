#!/bin/bash

self_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

srcfile=$1

[ -z $srcfile ] && { echo "Error: no source file" >&2; exit 2; }

export GOPATH=$self_dir

go run $srcfile

