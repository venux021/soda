#!/bin/bash

self_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

exefile=$1

[ -z $exefile ] && { echo "Error: no executable file" >&2; exit 2; }

export LD_LIBRARY_PATH=$this_dir/src/soda/leetcode:$LD_LIBRARY_PATH

ASAN_OPTIONS="detect_leaks=0" ./$exefile
