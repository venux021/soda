#ifndef _LEETCODE_BITREE
#define _LEETCODE_BITREE

#include <queue>
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
    TreeNode* load(string input) {
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
    
            trimLeftTrailingSpaces(item);
            if (item != "null") {
                int leftNumber = stoi(item);
                node->left = new TreeNode(leftNumber);
                nodeQueue.push(node->left);
            }
    
            if (!getline(ss, item, ',')) {
                break;
            }
    
            trimLeftTrailingSpaces(item);
            if (item != "null") {
                int rightNumber = stoi(item);
                node->right = new TreeNode(rightNumber);
                nodeQueue.push(node->right);
            }
        }
        return root;
    }
};


} // namespace leetcode

#endif
