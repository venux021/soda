#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

export GOPATH=$self_dir

cd $self_dir
go build ./...
