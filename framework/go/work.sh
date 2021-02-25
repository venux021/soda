#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    soda go [options]

options:
    new <testname>
        create source file with name <testname>.go
    $command_run_help

EOF
    exit 1
}

self_dir=$(cd $(dirname $0) && pwd)
framework_dir=$(dirname $self_dir)
source $framework_dir/common/bashlib.sh || exit

cmd=$1
[ -z $cmd ] && usage

exec_test()
{
    local exefile=$1
    [ -z $exefile ] && usage
    [ -e $exefile ] || { echo "$exefile not exist" >&2; exit; }
    run_test go "$@"
}

case $cmd in
    new)
        testname=$2
        [ -z $testname ] && usage
        testname=${testname%.go}
        target_file=${testname}.go
        template_file=$self_dir/bootstrap.go
        create_source_file $template_file $target_file
        ;;
    run)
        testname=$2
        [ -z $testname ] && usage
        exefile=${testname}.go
        shift; shift
        exec_test $exefile "$@"
        ;;
    *)
        usage
        ;;
esac

