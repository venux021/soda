#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

bash $self_dir/caller.sh compile "$1"
