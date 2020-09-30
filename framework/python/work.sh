#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    soda python [options]

options:
    new <testname>
        create source file with name <testname>.py

    run <testname> [--testcase <files>] [--verbose]
        run test case
        
        --testcase <files>    test case files, separated by ':', default is 'test_data'
        --verbose             show test request & response

    exec <exefile> [options]
        run executable file, options same as command 'run'
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
    run_test python "$@"
}

case $cmd in
    new)
        testname=$2
        [ -z $testname ] && usage
        testname=${testname%.py}
        target_file=${testname}.py
        template_file=$self_dir/src/soda/unittest/bootstrap.py
        create_source_file $template_file $target_file
        ;;
    run)
        testname=$2
        [ -z $testname ] && usage
        exefile=${testname}.py
        shift; shift
        exec_test $exefile "$@"
        ;;
    exec)
        shift
        exec_test "$@"
        ;;
    *)
        usage
        ;;
esac

