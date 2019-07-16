#ifndef _LEETCODE_BITREE
#define _LEETCODE_BITREE

#include <queue>
#include <sstream>
using namespace std;

#include "string.h"

namespace leetcode {

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BiTree {
public:
    static TreeNode* load(string input) {
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

    static string toString(TreeNode *root) {
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

    static void destroy(TreeNode *root) {
        if (root) {
            destroy(root->left);
            destroy(root->right);
        }
        delete root;
    }
};


} // namespace leetcode

#endif
