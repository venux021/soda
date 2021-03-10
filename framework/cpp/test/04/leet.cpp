//#include <bits/stdc++.h>
#include <vector>
#include <optional>
#include <iostream>
#include <string>

// #include "soda/leetcode/leetcode.h"
#include "soda/unittest/work.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution
// class Solution {};
class TopVotedCandidate {
    int N;
    vector<int> times;
    vector<int> winner;
public:
    TopVotedCandidate(vector<int>& persons, vector<int>& times):
        N(persons.size()), times(times), winner(persons.size())
    {
        vector<int> counter(N+1, 0);
        int win = 0;
        for (int i = 0; i < N; ++i) {
            if (++counter[persons[i]] >= counter[win]) {
                win = persons[i];
            }
            winner[i] = win;
        }
    }
    
    int q(int t) {
        if (t >= times.back()) {
            return winner[N-1];
        }
        int low = 0, high = N-1;
        while (low < high) {
            int mid = (low + high) / 2;
            if (t <= times[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return t == times[low] ? winner[low] : winner[low-1];
    }
};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

struct Params {
    vector<int> persons;
    vector<int> times;
    vector<int> qs;
};

class Solution {
public:
    vector<optional<int>> doTest(vector<string>& commands, Params& params) {
        vector<optional<int>> res;
        TopVotedCandidate* tvc = nullptr;
        for (int i = 0; i < commands.size(); ++i) {
            if (commands[i] == "TopVotedCandidate") {
                tvc = new TopVotedCandidate(params.persons, params.times);
                res.emplace_back();
            } else {
                res.emplace_back(tvc->q(params.qs[i]));
            }
        }
        delete tvc;
        return res;
    }
};

USE_CUSTOM_SERIAL(Params)

class ParamsParser : public TypedDataParser<Params> {
public:
    Params parse(JsonPointer jp) override {
        Params params;
        auto p0 = jp[0].get<vector<vector<int>>>();
        params.persons = p0[0];
        params.times = p0[1];
        params.qs.push_back(-1);
        for (int i = 1; i < jp.size(); ++i) {
            auto v = jp[i].get<vector<int>>();
            params.qs.push_back(v[0]);
        }
        return params;
    }
};

// [optional] use custom type with parser and serializer,
// and if you use this macro, may be you should define your own validator
// USE_CUSTOM_SERIALIZER(type)

// [optional] instantiate json access type. This will increase compile time
// #include "soda/unittest/json_access.h"
// SODA_JSON_ACCESS_TYPE(type)

int main()
{
    // [1] create by class member function
    Solution su;
    auto work = WorkFactory::create(su, &Solution::doTest);
    //
    // [2] or, create by ordinary function
    // auto work = WorkFactory::create(function);

    // work->setValidator(validate);
    work->setCompareSerial(true);
    work->setArgParser<1>(new ParamsParser);
    // work->setArgParser<0,from_type>(parse_func);
    // work->setResultParser<from_type>(parse_func);
    // work->setResultSerializer(serial_func);
    work->run();
    delete work;
    return 0;
}
