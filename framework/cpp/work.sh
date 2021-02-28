#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat>&2 << EOF
usage:
    soda cpp [options]

options:
    new <testname>
        create source file with name <testname>.cpp

    make <testname> 
        build executable

    run <testname>
        run executable

    clean <testname>
        clean intermediate files

EOF
    exit 1
}

self_dir=$(cd $(dirname $0) && pwd)
framework_dir=$(dirname $self_dir)
source $framework_dir/common/bashlib.sh || exit

[ -e $self_dir/setup_env.sh ] || cp $self_dir/_setup_env.sh $self_dir/setup_env.sh
source $self_dir/setup_env.sh || exit

cmd=$1
[ -z $cmd ] && usage

testname=$2
makefile=Makefile.gen.$testname

assert_testname()
{
    [ -z $testname ] && usage
}

assert_testname
case $cmd in
    new)
        template_file=$self_dir/src/soda/unittest/bootstrap.cpp
        create_source_file $template_file ${testname}.cpp
        ;;
    make)
        bash $self_dir/gen-makefile.sh -c $testname > $makefile
        make -f $makefile
        ;;
    run)
        execfile=${testname}.out
        [ -e $execfile ] || { echo "Error: no executable file" >&2; exit 2; }
        export LD_LIBRARY_PATH=$self_dir/src/soda/leetcode:$self_dir/src/soda/unittest:$LD_LIBRARY_PATH
        ASAN_OPTIONS="detect_leaks=0" ./$execfile
        ;;
    clean)
        make -f $makefile clean
        rm $makefile
        ;;
    *)
        usage
        ;;
esac

