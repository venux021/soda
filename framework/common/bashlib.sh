this_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)
framework_dir=$(dirname $this_dir)

create_source_file()                                                                                    
{                                                                                                       
    local template_file=$1                                                                                    
    local target_file=$2                                                                                      
    [ -z $target_file ] && usage                                                                        
    [ -e $target_file ] && { echo "Error: $target_file exists" >&2; exit 2; }                           
    cat $template_file > $target_file && echo "$target_file OK"                                         
}

run_test()
{
    export PYTHONPATH="$framework_dir/python/src:$PYTHONPATH"
    runner=soda.unittest.tester
    python3 -m $runner "$@"
}
