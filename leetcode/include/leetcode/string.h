#ifndef _LEETCODE_STRING
#define _LEETCODE_STRING

#include <string>
using namespace std;

namespace leetcode {

class String {
public:

    static void trimLeftTrailingSpaces(string &input) {
        input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
            return !isspace(ch);
        }));
    }
    
    static void trimRightTrailingSpaces(string &input) {
        input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
            return !isspace(ch);
        }).base(), input.end());
    }

    static string trim(const string &str) {
        string temp = str;
        trimLeftTrailingSpaces(temp);
        trimRightTrailingSpaces(temp);
        return temp;
    }

    static vector<string> loadArray(string &input) {
        int pos = 0;
        return _loadArray(input, pos);
    }

    static vector<string> loadArray(istream &in) {
        string line;
        if (getline(in, line)) {
            return loadArray(line);
        } else {
            throw "content loading error";
        }
    }

    static vector<vector<string>> loadArray2d(istream &in) {
        string line;
        if (getline(in, line)) {
            return loadArray2d(line);
        } else {
            throw "content loading error";
        }
    }

    static vector<vector<string>> loadArray2d(string &input) {
        int pos = 0, end = int(input.size());
        skipWhitespace(input, pos);
        if (pos == end || input[pos] != '[') {
            throw "Invalid json string format";
        }
        ++pos;  // skip '['
        vector<vector<string>> arr2d;
        while (true) {
            skipWhitespace(input, pos);
            if (input[pos] == '[') {
                arr2d.push_back(_loadArray(input, pos));
            } else if (input[pos] == ']') {
                break;
            } else {
                throw "Invalid json string format";
            }
            skipWhitespace(input, pos);
            if (input[pos] == ',') {
                ++pos;
            } else if (input[pos] == ']') {
                break;
            } else {
                throw "Invalid json string format";
            }
        }
        ++pos;  // skip ']'
        return arr2d;
    }

private:
    static void skipWhitespace(string &input, int &pos) {
        int end = int(input.size());
        while (pos < end and input[pos] == ' ') {
            ++pos;
        }
    }

    static vector<string> _loadArray(string &input, int &pos) {
        int end = int(input.size());
        skipWhitespace(input, pos);
        if (pos == end || input[pos] != '[') {
            throw "Invalid json string format";
        }
        ++pos; // skip '['
        skipWhitespace(input, pos);
        vector<string> strArr;
        string temp;
        while (parseString(input, pos, temp)) {
            strArr.push_back(temp);
            skipWhitespace(input, pos);
            if (input[pos] == ',') {
                ++pos;
            } else if (input[pos] == ']') {
                break;
            } else {
                throw "Invalid json string format";
            }
        }
        if (input[pos] != ']') {
            throw "Invalid json string format";
        }
        ++pos;  // skip ']'
        return strArr;
    }

    static bool parseString(string &input, int &pos, string &out) {
        skipWhitespace(input, pos);
        if (pos == int(input.size()) || input[pos] != '"') {
            return false;
        }
        ++pos;  // skip '"'
        int start = pos;
        while (pos < int(input.size())) {
            if (input[pos] == '\\') {
                pos += 2;
            } else if (input[pos] == '"') {
                break;
            } else {
                ++pos;
            }
        }
        if (pos == int(input.size())) {
            return false;
        }
        int end = pos;
        ++pos;  // skip '"'
        out = input.substr(start, end - start);
        return true;
    }

};

} // leetcode

#endif
