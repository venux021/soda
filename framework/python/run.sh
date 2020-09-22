#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

source $self_dir/setup_env.sh || exit 1

srcfile=$1

[ -z $srcfile ] && { echo "Error: no source file" >&2; exit 2; }

python3 $srcfile
