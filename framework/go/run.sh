#!/bin/bash

self_dir=$(cd -P $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)

execfile=$1

[ -z $execfile ] && { echo "Error: no executable file" >&2; exit 2; }

./$execfile

