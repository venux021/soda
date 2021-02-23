this_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

export SODA_INCLUDE="-I. -I$this_dir/include -I$this_dir/src"
export SODA_CPP_FLAGS="-std=c++17 -Wreturn-type -fsanitize=address -fsanitize=signed-integer-overflow"
