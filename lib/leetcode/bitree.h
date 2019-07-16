#ifndef _LEETCODE_BITREE
#define _LEETCODE_BITREE

#include <string>
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
    static TreeNode* load(string input);

    static string toString(TreeNode *root);

    static void destroy(TreeNode *root);

};

} // namespace leetcode

#endif
