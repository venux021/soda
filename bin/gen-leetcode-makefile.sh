#!/bin/bash

usage()
{
    cat << EOF
usage:
    $(basename $0) -b <base-path> -c <case-name>
EOF
    exit 1
}

while getopts ':b:c:' option; do
    case $option in
        b)
            base_path="$OPTARG"
            ;;
        c)
            case_name="$OPTARG"
            ;;
        \?)
            usage
    esac
done

[ -z $base_path -o -z $case_name ] && usage

cat << EOF
SOURCES = ${case_name}.cpp
OBJS = \$(SOURCES:.cpp=.o)
INCLUDE = -I. -I${base_path}/lib
LIBRARY = -L${base_path}/lib/leetcode -lleetcode
CC = g++
CPPFLAGS = -std=c++17 \$(INCLUDE) -Wreturn-type -fsanitize=address -fsanitize=signed-integer-overflow
TARGET = ${case_name}.out

all: \$(TARGET)

COMMON_LIB:
	@cd ${base_path}/lib/leetcode; \\
	make; cd -;

EOF

cat <<"EOF"
%.d: %.cpp
	@set -e; rm -f $@; \
	$(CC) $(CPPFLAGS) -MM $< > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

sinclude $(SOURCES:.cpp=.d)

$(TARGET): $(OBJS) COMMON_LIB
	$(CC) $(CPPFLAGS) -o $(TARGET) $(OBJS) $(LIBRARY)

clean:
	rm -f *.o $(TARGET) *.d
EOF

