#ifndef _LEETCODE_STRING
#define _LEETCODE_STRING

namespace leetcode {

class String {
public:
    static void trimLeftTrailingSpaces(string &input);
    
    static void trimRightTrailingSpaces(string &input);

    static string trim(const string &str);
};

} // leetcode

#endif
