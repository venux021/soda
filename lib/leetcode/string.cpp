#include <algorithm>
#include <string>
using namespace std;

#include "string.h"

namespace leetcode {

void String::trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void String::trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

string String::trim(const string &str) {
    string temp = str;
    trimLeftTrailingSpaces(temp);
    trimRightTrailingSpaces(temp);
    return temp;
}

} // namespace leetcode
