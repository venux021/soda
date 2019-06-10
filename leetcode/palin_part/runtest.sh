#!/bin/bash

set -x
g++ -pg -std=c++14 part.cpp && time ./a.out
gprof a.out gmon.out -p > prof
