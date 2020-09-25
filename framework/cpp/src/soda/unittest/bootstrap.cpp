#include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/unittest.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [0]: implement class Solution
// class Solution {};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

class TestJob {
public:
    // step [1]: set result object type
    using ResultType = ...;
    // setp [2]: set serialized result type
    using ResultSerialType = ResultType;

    // step [3]: call solution
    void execute(const TestRequest& req, TestResponse& resp) {
        // TODO

        resp.setResult(serialize(res));
    }

    // step [4]: result serializer
    ResultSerialType serialize(const ResultType& res) {
        return res;
    }

    // step [5]: implement result validation
    bool validate(const TestRequest& req, const TestResponse& resp) {
        // It's OK for most scenario, but maybe sometimes you'll need to do comparison in their original type
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

    TestJob job;

    auto startMicro = chrono::steady_clock::now();
    job.execute(req, resp);
    auto endMicro = chrono::steady_clock::now();
    auto elapseMicro = chrono::duration_cast<chrono::microseconds>(endMicro - startMicro).count();

    resp.elapse = elapseMicro / 1000.0;

    if (req.hasExpected()) {
        resp.success = job.validate(req, resp);
    } else {
        resp.success = true;
    }

    cout << resp.toJSONString();

    return 0;
}
