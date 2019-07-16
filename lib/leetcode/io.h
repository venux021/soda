#ifndef _LEETCODE_IO_H
#define _LEETCODE_IO_H

#include <iostream>
#include <string>
using namespace std;

namespace leetcode {

class IO {
public:
    static int loadInt(istream &in) {
        string line;
        return getline(in, line) ? stoi(line) : 0;
    }
};

}  // namespace leetcode

#endif
