// #include <bits/stdc++.h>
#include <vector>
#include <string>
#include <deque>
#include "soda/leetcode/leetcode.h"
#include "soda/unittest/work.h"

using namespace std;
using namespace soda::leetcode;
using namespace soda::unittest;

// step [1]: implement class Solution

namespace {
    const auto __ = []() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        return 0;
    }();
}

class CBTInserter {
    deque<TreeNode*> qu;
    TreeNode* root;
public:
    CBTInserter(TreeNode* root): qu{}, root{root} {
        qu.push_back(root);
        while (!qu.empty()) {
            auto node = qu.front();
            if (!node->left) {
                break;
            }
            qu.push_back(node->left);
            if (!node->right) {
                break;
            }
            qu.push_back(node->right);
            qu.pop_front();
        }
    }
    
    int insert(int v) {
        auto node = new TreeNode(v);
        auto head = qu.front();
        qu.push_back(node);
        if (!head->left) {
            head->left = node;
        } else {
            head->right = node;
            qu.pop_front();
        }
        return head->val;
    }
    
    TreeNode* get_root() {
        return root;
    }
};

class Solution {
public:
    vector<JsonProxy> doTest(vector<string>& commands, vector<JsonProxy>& params) {
        vector<JsonProxy> res;
        unique_ptr<CBTInserter> cb;
        for (int i = 0; i < commands.size(); ++i) {
            if (commands[i] == "CBTInserter") {
                auto treeData = params[i][0].get<vector<optional<int>>>();
                cb = make_unique<CBTInserter>(TreeFactory::create(treeData));
                res.emplace_back(nullptr);
            } else if (commands[i] == "insert") {
                int k = params[i].get<vector<int>>()[0];
                res.emplace_back(cb->insert(k));
            } else {
                auto root = cb->get_root();
                res.emplace_back(TreeFactory::dump(root));
            }
        }
        return res;
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
    // work->setArgParser<0,from_type>(parse_func);
    // work->setResultParser<from_type>(parse_func);
    // work->setResultSerializer(serial_func);
    work->run();
    delete work;
    return 0;
}
