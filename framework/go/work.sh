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

    build <testname>
        build test case
    $command_run_help

EOF
    exit 1
}

self_dir=$(cd $(dirname $0) && pwd)
framework_dir=$(dirname $self_dir)
source $framework_dir/common/bashlib.sh || exit

cmd=$1
[ -z $cmd ] && usage

testname=${2%.go}
srcfile=${testname}.go
execfile=${srcfile}.out

exec_test()
{
    shift; shift  # skip <cmd> <testname>
    [ -e $execfile ] || { echo "$execfile not exist" >&2; exit; }
    run_test go $execfile "$@"
}

assert_testname()
{
    [ -z $testname ] && usage
}

do_build()
{
    [ -e $execfile ] && rm $execfile
    GOPATH=$self_dir go build -o $execfile $srcfile
}

case $cmd in
    new)
        assert_testname
        create_source_file $self_dir/bootstrap.go $srcfile
        ;;
    build)
        assert_testname
        do_build
        ;;
    run)
        assert_testname
        exec_test "$@"
        ;;
    go)
        do_build && exec_test "$@"
        ;;
    *)
        usage
        ;;
esac

