#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    soda cpp [options]

options:
    new <testname>
        create source file with name <testname>.cpp

    compile <testname> 
        compile test case

    run <testname> [<datefile>...]
        run test case, default data file is 'test_data'

    go <testname> [<datafile>...] 
        compile && run

    clean <testname>
        clean intermediate files

    exec <exefile> [<datefile>...]
        run executable file, default data file is 'test_data'
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

exec_test()
{
    local exefile=$1
    [ -z $exefile ] && usage
    [ -x $exefile ] || { echo "$exefile is not executable" >&2; exit; }
    run_test cpp "$@"
}

do_compile()
{
    testname=$1
    [ -z $testname ] && usage
    testname=${testname%.cpp}
    makefile=Makefile.gen.$testname
    bash $self_dir/gen-makefile.sh -c $testname > $makefile
    make -f $makefile
}

do_run()
{
    testname=$1
    [ -z $testname ] && usage
    exefile=${testname}.out
    shift
    exec_test $exefile "$@"
}

case $cmd in
    new)
        testname=$2
        [ -z $testname ] && usage
        testname=${testname%.cpp}
        target_file=${testname}.cpp
        template_file=$self_dir/src/soda/unittest/bootstrap.cpp
        create_source_file $template_file $target_file
        ;;
    compile)
        shift
        do_compile "$@"
        ;;
    run)
        shift
        do_run "$@"
        ;;
    go)
        shift
        do_compile "$@" && do_run "$@"
        ;;
    clean)
        testname=$2
        [ -z $testname ] && usage
        makefile=Makefile.gen.$testname
        make -f $makefile clean
        rm $makefile
        ;;
    exec)
        shift
        exec_test "$@"
        ;;
    *)
        usage
        ;;
esac

