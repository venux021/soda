#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

source $self_dir/setup_env.sh || exit

classname=$1

assert_framework

java -cp $(get_classpath) $classname
