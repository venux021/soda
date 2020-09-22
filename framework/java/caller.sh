#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    $cmd compile <source file>
    $cmd run <class name>
EOF
    exit 1
}

cmd=$1
[ -z $cmd ] && usage

self_dir=$(cd $(dirname $0) && pwd)

source $self_dir/setup_env.sh || exit 1

classfile=$1

[ -z $classfile ] && { echo "Error: no class file" >&2; exit 2; }

lib_dir=$self_dir/soda-lib

[ -e $lib_dir ] || { bash $self_dir/deploy.sh || exit; }
ls $lib_dir/*.jar >/dev/null 2>&1 || { bash $self_dir/deploy.sh; exit; }

ls $lib_dir/*.jar >/dev/null 2>&1 || { echo "Error: unable to build java framework" >&2; exit; }

classpath=.
for jar in $(ls $lib_dir); do
    classpath="$classpath:$lib_dir/$jar"
done

if [ "$cmd" == "compile" ]; then
    srcfile=$2
    [ -z $srcfile ] && usage
    javac -cp $classpath $srcfile
elif [ "$cmd" == "run" ]; then
    classname=$2
    [ -z $classname ] && usage
    java -cp $classpath $classname
fi
