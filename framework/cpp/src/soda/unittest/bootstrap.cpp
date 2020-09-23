#include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/unittest.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

// step [0]: implement class Solution
// class Solution {};

// step [1]: implement validate
template <typename T>
bool validate(const T& res, const T& answer)
{
    return res == answer;
}

int main()
{
    string line, content;
    while (getline(cin, line)) {
        content += line;
    }

    UnitTestRequest req(content);

    // step [2]: deserialize arguments
    // TODO auto arg0 = req.arg<T0>(0);

    auto startMicro = std::chrono::steady_clock::now();

    Solution su;
    // step [3]: invoke solution function
    // TODO auto res = su.someMethod(arg0, arg1, ...);

    auto endMicro = std::chrono::steady_clock::now();
    auto elapseMicro = std::chrono::duration_cast<std::chrono::microseconds>(endMicro - startMicro).count();

    UnitTestResponse resp;
    resp.id = req.id();
    resp.elapse = elapseMicro / 1000.0;

    if (req.hasAnswer()) {
        // step [4]: deserialize answer object
        // TODO auto answer = _deserialize(req.answer<T>());
        resp.success = validate(res, answer);
    } else {
        resp.success = true;
    }

    // step [5]: serialize result object
    // TODO auto serialRes = _serialize(res);
    resp.setResult(serialRes);

    cout << resp.toJSONString();

    return 0;
}
