#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

export GOPATH=$self_dir

# for go1.16
export GO111MODULE=auto

cd $self_dir
go build ./src/...
