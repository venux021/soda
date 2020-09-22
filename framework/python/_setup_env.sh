self_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)
src_dir=$self_dir/src
export PYTHONPATH="$src_dir:$PYTHONPATH"
