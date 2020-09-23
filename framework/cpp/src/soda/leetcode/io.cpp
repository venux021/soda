#include "io.h"

namespace soda::leetcode {

int IO::loadInt(istream &in) {
    string line;
    return getline(in, line) ? stoi(line) : 0;
}

} // namespace soda::leetcode
