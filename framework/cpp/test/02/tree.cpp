// #include <bits/stdc++.h>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/work.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution
// class Solution {};
class Solution {
public:
    TreeNode* mirror(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        mirror(root->left);
        mirror(root->right);
        std::swap(root->left, root->right);
        return root;
    }
};

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

bool validate(TreeNode* e, TreeNode* r)
{
    if (!e && !r) {
        return true;
    } else if (e && r) {
        return e->val == r->val && validate(e->left, r->left) && validate(e->right, r->right);
    }
    return false;
}

int main()
{
    // [1] create by class member function
    Solution su;
    auto work = WorkFactory::create(su, &Solution::mirror);
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
