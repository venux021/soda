#!/bin/bash

usage()
{
    local cmd=$(basename $0)
    cat << EOF
usage:
    soda java [-s|-r] [options]

    -s: use server mode
    -r: restart server, then use server mode

options:
    new <testname>
        create source file with name <testname>.java

    compile <testname> 
        compile test case
    $command_run_help

    go <testname> [options] 
        compile && run, options same as command 'run'

    exec <classname> [options]
        run test case by class name, options same as command 'run'

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

server_mode=no
if [ "$cmd" == "-s" -o "$cmd" == '-r' ]; then
    server_mode=yes
    [ "$cmd" == "-r" ] && $self_dir/server.sh stop
    shift
    cmd=$1
fi

exec_test()
{
    local classname=$1
    [ -z $classname ] && usage
    if [ "$server_mode" == 'yes' ]; then
        set -e
        $self_dir/server.sh start
        runpath=$(pwd)
        curl -d "runpath=$runpath" "http://localhost:$server_port/soda/java/setup" && echo
        export SODA_JAVA_SERVER_MODE=yes
        set +e
    fi
    run_test java "$@"
}

do_compile()
{
    testname=$1
    [ -z $testname ] && usage
    srcfile=${testname}.java
    assert_framework
    echo "Compiling $srcfile ..."
    javac -cp $(get_classpath) $SODA_JAVA_COMPILE_OPTION $srcfile && echo "Compile $srcfile OK"
}

case $cmd in
    new)
        testname=$2
        [ -z $testname ] && usage
        testname=${testname%.java}
        target_file=${testname}.java
        template_file=$self_dir/src/main/java/soda/unittest/__Bootstrap__.java
        create_source_file $template_file $target_file
        classname=$testname
        echo "import soda.unittest.*;" > ${classname}.tmp
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
    go)
        testname=$2
        do_compile $testname || exit
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

