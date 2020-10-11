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
    string line, content;
    while (getline(cin, line)) {
        content += line;
    }

    TestRequest req(content);
    TestResponse resp;
    resp.id = req.id();

    auto job = new TestJob();

    auto startMicro = chrono::steady_clock::now();
    job->run(req, resp);
    auto endMicro = chrono::steady_clock::now();
    auto elapseMicro = chrono::duration_cast<chrono::microseconds>(endMicro - startMicro).count();

    resp.elapse = elapseMicro / 1000.0;

    if (req.hasExpected()) {
        resp.success = job->validate(req, resp);
    } else {
        resp.success = true;
    }

    cout << resp.toJSONString();

    delete job;
    return 0;
}
