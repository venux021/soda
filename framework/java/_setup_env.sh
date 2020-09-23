this_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

#export JAVA_HOME=$JAVA_HOME

get_classpath()
{
    local lib_dir=$this_dir/soda-lib
    
    [ -e $lib_dir ] || { bash $this_dir/deploy.sh || exit; }
    ls $lib_dir/*.jar >/dev/null 2>&1 || { bash $this_dir/deploy.sh; exit; }
    
    ls $lib_dir/*.jar >/dev/null 2>&1 || { echo "Error: unable to build java framework" >&2; exit; }
    
    local classpath=.
    for jar in $(ls $lib_dir); do
        classpath="$classpath:$lib_dir/$jar"
    done

    echo $classpath
}
