#ifndef _LEETCODE_STRING
#define _LEETCODE_STRING

#include <algorithm>
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
};

} // leetcode

#endif
