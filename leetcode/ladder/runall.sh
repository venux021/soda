#!/bin/bash

set -x
g++ -std=c++14 bladder.cpp -o b.out
g++ -std=c++14 cladder.cpp -o c.out
time ./b.out
time ./c.out
