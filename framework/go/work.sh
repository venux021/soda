#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat>&2 << EOF
usage:
    soda go [options]

options:
    new <testname>
        create source file with name <testname>.go

    make <testname> 
        build executable

    run <testname>
        run executable

EOF
    exit 1
}

self_dir=$(cd $(dirname $0) && pwd)
framework_dir=$(dirname $self_dir)
source $framework_dir/common/bashlib.sh || exit

cmd=$1
[ -z $cmd ] && usage

testname=$2
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

assert_testname
case $cmd in
    new)
        create_source_file $self_dir/bootstrap.go $srcfile
        ;;
    make)
        [ -e $execfile ] && rm $execfile
        GOPATH=$self_dir go build -o $execfile $srcfile && echo "Build success."
        ;;
    run)
        ./$execfile
        ;;
    *)
        usage
        ;;
esac

