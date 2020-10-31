#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    soda scala [options]

options:
    new <testname>
        create source file with name <testname>.scala

    compile <testname> 
        compile test case
    $command_run_help

    exec <exefile> [options]
        run executable file, options same as command 'run'

EOF
    exit 1
}

self_dir=$(cd $(dirname $0) && pwd)
framework_dir=$(dirname $self_dir)
source $framework_dir/common/bashlib.sh || exit

source $self_dir/../java/setup_env.sh || exit

cmd=$1
[ -z $cmd ] && usage

exec_test()
{
    local classname=$1
    [ -z $classname ] && usage
    run_test scala "$@"
}

do_compile()
{
    testname=$1
    [ -z $testname ] && usage
    srcfile=${testname}.scala
    assert_framework
    scalac -deprecation -cp $(get_classpath) $srcfile && echo "Compile $srcfile OK"
}

case $cmd in
    new)
        testname=$2
        [ -z $testname ] && usage
        testname=${testname%.scala}
        target_file=${testname}.scala
        template_file=$self_dir/src/main/scala/soda/unittest/__Bootstrap__.scala
        create_source_file $template_file $target_file
        classname=$testname
        echo "import soda.unittest._;" > ${classname}.tmp
        cat $target_file | grep -v '^package ' | sed "s/__Bootstrap__/$classname/g" >> ${classname}.tmp
        mv ${classname}.tmp $target_file
        ;;
    compile)
        testname=$2
        do_compile $testname
        ;;
    run)
        shift
        exec_test "$@"
        ;;
    exec)
        shift
        exec_test "$@"
        ;;
    *)
        usage
        ;;
esac

