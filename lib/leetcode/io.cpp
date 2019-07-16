#include "io.h"

namespace leetcode {

int IO::loadInt(istream &in) {
    string line;
    return getline(in, line) ? stoi(line) : 0;
}

} // namespace leetcode
