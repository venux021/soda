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

    static vector<int> loadIntArray(string input) {
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

    static string toString(const vector<vector<int>> &arr2d) {
        if (arr2d.size() == 0) {
            return "[]";
        }

        string s;
        for (int index = 0; index < int(arr2d.size()); ++index) {
            s += toString(arr2d[index]) + ", ";
        }
        return "[" + s.substr(0, s.size()-2) + "]";
    }

    static vector<vector<int>> loadIntArray2D(istream &in) {
        string line;
        return getline(in, line) ? loadIntArray2D(line) : vector<vector<int>>();
    }

    static vector<vector<int>> loadIntArray2D(string input) {
        String::trimLeftTrailingSpaces(input);
        String::trimRightTrailingSpaces(input);
        vector<vector<int>> arr2d;
        int i = 1; // skip '['
        while (input[i] != ']') {
            while (input[i] != '[' && input[i] != ']') {
                ++i;
            }
            if (input[i] == '[') {
                int j = i+1;
                while (input[j] != ']') {
                    ++j;
                }
                arr2d.push_back(loadIntArray(input.substr(i,j-i+1)));
                i = j + 1;
            }
        }
        return arr2d;
    }
};

} // namespace leetcode

#endif
