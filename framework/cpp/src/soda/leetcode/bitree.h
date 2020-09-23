#ifndef _SODA_LEETCODE_BITREE_H_
#define _SODA_LEETCODE_BITREE_H_

#include <string>
using namespace std;

#include "string.h"

namespace soda::leetcode {

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

} // namespace soda::leetcode

#endif
