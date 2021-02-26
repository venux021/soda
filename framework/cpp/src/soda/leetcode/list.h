#ifndef _SODA_LEETCODE_LIST_H_
#define _SODA_LEETCODE_LIST_H_

#include <utility>
#include <vector>

namespace soda::leetcode {

template <typename T>
struct SingleListNode {
    T val;
    SingleListNode<T>* next{nullptr};
    SingleListNode(const T& x): val{x} {}
    SingleListNode(T&& x): val{std::move(x)} {}
    SingleListNode(): SingleListNode(T()) {}
};

template <typename T>
struct SingleListFactory {
    using Node = SingleListNode<T>;

    static Node* create(const std::vector<T>& data) {
        Node head(-1);
        Node* tail = &head;
        for (auto& val : data) {
            auto node = new Node(val);
            tail->next = node;
            tail = node;
        }
        return head.next;
    }

    static std::vector<T> dump(Node* head) {
        std::vector<T> data;
        for (; head; head = head->next) {
            data.emplace_back(head->val);
        }
        return data;
    }
};

using ListNode = SingleListNode<int>;
using ListFactory = SingleListFactory<int>;

// struct ListNode : public SingleListNode<int> {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(NULL) {}
// };

class List {
public:
    static ListNode *load(istream &in);
    
    static ListNode *load(string input);

    static string toString(ListNode *node);
};

class ListHelper {
public:

    static ListNode* create(const std::vector<int>& listData);

    static std::vector<int> dump(ListNode* head);

};

} // namespace soda::leetcode

#endif
