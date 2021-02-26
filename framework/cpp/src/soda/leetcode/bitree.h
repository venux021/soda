#ifndef _SODA_LEETCODE_BITREE_H_
#define _SODA_LEETCODE_BITREE_H_

#include <deque>
#include <optional>
#include <string>
#include <vector>
#include <utility>

namespace soda::leetcode {

template <typename T>
struct BiTreeNode {
    T val;
    BiTreeNode<T>* left {nullptr};
    BiTreeNode<T>* right {nullptr};

    BiTreeNode(const T& x): val{x} {}
    BiTreeNode(T&& x): val{std::move(x)} {}
    BiTreeNode(): BiTreeNode(T()) {}
};

template <typename T>
struct BiTreeFactory {
    using Node = BiTreeNode<T>;

    static Node* create(const std::vector<std::optional<T>>& treeData);

    static std::vector<std::optional<T>> dump(const Node* root);
};

using TreeNode = BiTreeNode<int>;
using TreeFactory = BiTreeFactory<int>;

// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
// };

class BiTree {
public:
    static TreeNode* load(std::string input);

    static std::string toString(TreeNode *root);

    static void destroy(TreeNode *root);

    static TreeNode* create(const std::vector<std::optional<int>>& treeData);

    static std::vector<std::optional<int>> inLevelOrder(const TreeNode* root);

};

template <typename T>
BiTreeNode<T>* BiTreeFactory<T>::create(const std::vector<std::optional<T>>& data)
{
    if (data.size() == 0) {
        return nullptr;
    }

    auto root = new Node(*data[0]);
    int index = 1;
    std::deque<Node*> qu;
    qu.push_back(root);
    for (int index = 1; index < data.size(); ) {
        auto node = qu.front();
        qu.pop_front();
        if (data[index]) {
            node->left = new Node(*data[index]);
            qu.push_back(node->left);
        }
        ++index;
        if (index == data.size()) {
            break;
        }
        if (data[index]) {
            node->right = new Node(*data[index]);
            qu.push_back(node->right);
        }
        ++index;
    }
    return root;
}

template <typename T>
std::vector<std::optional<T>> BiTreeFactory<T>::dump(const Node* root)
{
    if (!root) {
        return {};
    }
    std::vector<const Node*> curr, next, order;
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

    std::vector<std::optional<int>> data;
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

#endif
