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

// step [2]: implement test job
class TestJob : public JobTemplate</*TODO result type*/, /*TODO result serial type*/> {
public:
    ResultType execute(const TestRequest& req, TestResponse& resp) override {
        // TODO
        cerr << "Not implemented" << endl;
    }

    ResultSerialType serialize(const ResultType& res) override {
        return res;
    }

    bool validate(const TestRequest& req, const TestResponse& resp) override {
        return req.getExpected<ResultSerialType>() == resp.getResult<ResultSerialType>();
    }
};

int main()
{
    TestJob job;
    Runner runner;
    runner.run(job);
    return 0;
}
