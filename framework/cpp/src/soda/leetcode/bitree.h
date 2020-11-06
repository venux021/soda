#ifndef _SODA_LEETCODE_BITREE_H_
#define _SODA_LEETCODE_BITREE_H_

#include <optional>
#include <string>
#include <vector>

namespace soda::leetcode {

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BiTree {
public:
    static TreeNode* load(std::string input);

    static std::string toString(TreeNode *root);

    static void destroy(TreeNode *root);

    static TreeNode* create(const std::vector<std::optional<int>>& treeData);

    static std::vector<std::optional<int>> inLevelOrder(const TreeNode* root);

};

} // namespace soda::leetcode

#endif
