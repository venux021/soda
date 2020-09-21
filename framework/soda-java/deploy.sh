#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)
soda_dir=$(cd $self_dir/../.. && pwd)
lib_dir=$soda_dir/lib

mvn clean package

cp target/soda-java-*.jar target/soda-java/

[ -e $lib_dir/soda-java ] && rm -r $lib_dir/soda-java

cp -r target/soda-java $lib_dir/
