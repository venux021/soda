#include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/work.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution
// class Solution {};
class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* h = nullptr;
        while (head) {
            auto n = head->next;
            head->next = h;
            h = head;
            head = n;
        }
        return h;
    }
};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

bool validate(ListNode* e, ListNode* r)
{
    while (e && r) {
        if (e->val != r->val) {
            return false;
        }
        e = e->next;
        r = r->next;
    }
    return e == r;
}

int main()
{
    // [1] create by class member function
    Solution su;
    auto work = WorkFactory::create(su, &Solution::reverse);
    //
    // [2] or, create by ordinary function
    // auto work = WorkFactory::create(function);

    work->setValidator(validate);
    // work->setCompareSerial(true);
    // work->setArgParser<0,from_type>(parse_func);
    // work->setResultParser<from_type>(parse_func);
    // work->setResultSerializer(serial_func);
    work->run();
    delete work;
    return 0;
}
