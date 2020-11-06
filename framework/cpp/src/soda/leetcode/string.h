#ifndef _SODA_LEETCODE_STRING_H_
#define _SODA_LEETCODE_STRING_H_

#include <string>

namespace soda::leetcode {

class String {
public:
    static void trimLeftTrailingSpaces(std::string &input);
    
    static void trimRightTrailingSpaces(std::string &input);

    static std::string trim(const std::string &str);
};

} // soda::leetcode

#endif
