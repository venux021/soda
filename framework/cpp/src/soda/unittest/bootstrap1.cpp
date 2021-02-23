#include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/unittest.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution
// class Solution {};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

int main()
{
    JobEntry::run(&Solution::someFunction);

    // JobEntry::runWithObjectCheck(&Solution::someFunction, validator_using_object);
    // OR
    // JobEntry::runWithSerialCheck(&Solution::someFunction, validator_using_serial);

    return 0;
}
