#include <queue>
#include <sstream>

#include "bitree.h"
#include "string.h"

using namespace std;

namespace soda::leetcode {

TreeNode* BiTree::load(string input) {
    String::trimLeftTrailingSpaces(input);
    String::trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    if (!input.size()) {
        return nullptr;
    }

    string item;
    stringstream ss;
    ss.str(input);

    getline(ss, item, ',');
    TreeNode* root = new TreeNode(stoi(item));
    queue<TreeNode*> nodeQueue;
    nodeQueue.push(root);

    while (true) {
        TreeNode* node = nodeQueue.front();
        nodeQueue.pop();

        if (!getline(ss, item, ',')) {
            break;
        }

        String::trimLeftTrailingSpaces(item);
        if (item != "null") {
            int leftNumber = stoi(item);
            node->left = new TreeNode(leftNumber);
            nodeQueue.push(node->left);
        }

        if (!getline(ss, item, ',')) {
            break;
        }

        String::trimLeftTrailingSpaces(item);
        if (item != "null") {
            int rightNumber = stoi(item);
            node->right = new TreeNode(rightNumber);
            nodeQueue.push(node->right);
        }
    }
    return root;
}

string BiTree::toString(TreeNode *root) {
    string res = "[";
    if (root) {
        vector<TreeNode*> buf;
        std::queue<TreeNode*> qu;
        qu.push(root);
        while (!qu.empty()) {
            auto node = qu.front();
            qu.pop();
            buf.push_back(node);
            if (node) {
                qu.push(node->left);
                qu.push(node->right);
            }
        }
        while (buf.size() && !buf.back()) {
            buf.pop_back();
        }
        for (int i = 0; i < int(buf.size()) - 1; ++i) {
            if (buf[i]) {
                res.append(to_string(buf[i]->val));
            } else {
                res.append("null");
            }
            res.push_back(',');
        }
        res.append(to_string(buf.back()->val));
    }
    res.push_back(']');
    return res;
}

void BiTree::destroy(TreeNode *root) {
    if (root) {
        destroy(root->left);
        destroy(root->right);
    }
    delete root;
}

TreeNode* BiTree::create(const vector<optional<int>>& data)
{
    if (data.size() == 0) {
        return nullptr;
    }

    auto root = new TreeNode(*data[0]);
    int index = 1;
    deque<TreeNode*> qu;
    qu.push_back(root);
    for (int index = 1; index < data.size(); ) {
        auto node = qu.front();
        qu.pop_front();
        if (data[index]) {
            node->left = new TreeNode(*data[index]);
            qu.push_back(node->left);
        }
        ++index;
        if (index == data.size()) {
            break;
        }
        if (data[index]) {
            node->right = new TreeNode(*data[index]);
            qu.push_back(node->right);
        }
        ++index;
    }
    return root;
}

vector<optional<int>> BiTree::inLevelOrder(const TreeNode* root)
{
    if (!root) {
        return {};
    }
    vector<const TreeNode*> curr, next, order;
    curr.emplace_back(root);
    while (curr.size()) {
        next.clear();
        for (auto node : curr) {
            order.push_back(node);
            if (node) {
                next.push_back(node->left);
                next.push_back(node->right);
            }
        }
        curr = next;
    }

    vector<optional<int>> data;
    int i = order.size() - 1;
    while (!order[i]) {
        --i;
    }
    for (int j = 0; j <= i; ++j) {
        if (order[j]) {
            data.emplace_back(order[j]->val);
        } else {
            data.emplace_back();
        }
    }
    return data;
}

} // namespace soda::leetcode
