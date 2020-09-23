#ifndef _SODA_LEETCODE_STRING_H_
#define _SODA_LEETCODE_STRING_H_

namespace soda::leetcode {

class String {
public:
    static void trimLeftTrailingSpaces(string &input);
    
    static void trimRightTrailingSpaces(string &input);

    static string trim(const string &str);
};

} // soda::leetcode

#endif
