#include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/unittest.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution
// class Solution {};
struct Input1 {
    int value;
    Input1(int value = 0): value{value} {}
};

struct Input2 {
    string text;
    Input2(const string& t = ""): text{t} {}
};

struct Output {
    int val;
    string str;
    Output(int v = 0, const string& s = ""): val{v}, str{s} {}
};

USE_CUSTOM_SERIAL(Input1)
USE_CUSTOM_SERIAL(Input2*)
USE_CUSTOM_SERIAL(Output)

class Solution {
public:
    Output gen(Input1 i1, Input2 *pi2) {
        return {i1.value, pi2->text};
    }
};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

Input1 arg_parse_0(int v) {
    return {v};
}

Input2* arg_parse_1(const string& s) {
    return new Input2(s);
}

Output rParse(const vector<string>& ss) {
    return {int(ss.size()), ss[0]};
}

vector<string> rSerial(const Output& out) {
    return vector<string>(out.val, out.str);
}

bool validate(Output& e, Output& r) {
    return e.val == r.val && e.str == r.str;
}

int main()
{
    // [1] create by class member function
    Solution su;
    auto work = WorkFactory::create(su, &Solution::gen);
    //
    // [2] or, create by ordinary function
    // auto work = WorkFactory::create(function);

    work->setValidator(validate);
    // work->setCompareSerial(true);
    work->setArgParser<0,int>(arg_parse_0);
    work->setArgParser<1,string>(arg_parse_1);
    work->setResultParser<vector<string>>(rParse);
    work->setResultSerializer(rSerial);
    work->run();
    delete work;
    return 0;
}
