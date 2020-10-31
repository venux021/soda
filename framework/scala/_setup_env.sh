this_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

java_dir=$(dirname $this_dir)/java

source $java_dir/setup_env.sh || exit

[ -z $SCALA_HOME ] && { echo "Error: SCALA_HOME is empty" >&2; exit 1; }

export SODA_SCALA_COMPILE_OPTION=

server_port=9202
