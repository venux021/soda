#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

. $self_dir/setup_env.sh

for d in leetcode unittest; do
    cd $self_dir/src/soda/$d
    make clean
    cd -
done
