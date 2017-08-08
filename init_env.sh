SELF_DIR=$(pwd)
echo $PYTHONPATH | grep -q $SELF_DIR || export PYTHONPATH="$SELF_DIR:$PYTHONPATH"
echo "Add $SELF_DIR to PYTHONPATH"

bin_dir=$SELF_DIR/bin
export PATH="$bin_dir:$PATH"
