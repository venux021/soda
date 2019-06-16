#ifndef _LEETCODE_ARRAY
#define _LEETCODE_ARRAY

#include <iostream>
#include <sstream>
#include <string>
using namespace std;

#include "string.h"

namespace leetcode {

class Array {
public:
    static vector<int> loadIntArray(istream &in) {
        string line;
        return getline(in, line) ? loadIntArray(line) : vector<int>();
    }

    static vector<int> loadIntArray(string &input) {
        vector<int> output;
        String::trimLeftTrailingSpaces(input);
        String::trimRightTrailingSpaces(input);
        input = input.substr(1, input.length() - 2);
        stringstream ss;
        ss.str(input);
        string item;
        char delim = ',';
        while (getline(ss, item, delim)) {
            output.push_back(stoi(item));
        }
        return output;
    }

    static string toString(const vector<int> &list, int length = -1) {
        if (length == -1) {
            length = list.size();
        }

        if (length == 0) {
            return "[]";
        }

        string result;
        for(int index = 0; index < length; index++) {
            int number = list[index];
            result += to_string(number) + ", ";
        }
        return "[" + result.substr(0, result.length() - 2) + "]";
    }
};

} // namespace leetcode

#endif
