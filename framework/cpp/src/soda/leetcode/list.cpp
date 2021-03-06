#include <iostream>
#include <string>
using namespace std;

#include "array.h"
#include "list.h"

namespace soda::leetcode {

ListNode *List::load(istream &in) {
    string line;
    return getline(in, line) ? load(line) : nullptr;
}

ListNode *List::load(string input) {
    // Generate list from the input
    vector<int> list = Array::load<int>(input);

    // Now convert that list into linked list
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}

string List::toString(ListNode *node) {
    if (node == nullptr) {
        return "[]";
    }

    string result;
    while (node) {
        result += to_string(node->val) + ", ";
        node = node->next;
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

ListNode* ListHelper::create(const std::vector<int>& listData)
{
    return ListFactory::create(listData);
}

std::vector<int> ListHelper::dump(ListNode* head)
{
    return ListFactory::dump(head);
}

} // namespace soda::leetcode
