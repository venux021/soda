#ifndef _LEETCODE_LIST
#define _LEETCODE_LIST

#include <iostream>
#include <string>
using namespace std;

#include "array.h"

namespace leetcode {

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class List {
public:

    static ListNode *load(istream &in) {
        string line;
        return getline(in, line) ? load(line) : nullptr;
    }
    
    static ListNode *load(string input) {
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

    static string toString(ListNode *node) {
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
};

struct ListHelper {
    static ListNode *create(const vector<int> &nums)
    {
        ListNode head{0}, *tail = &head;
        for (int v : nums) {
            auto node = new ListNode(v);
            tail->next = node;
            tail = node;
        }
        return head.next;
    }
    
    static void print(ListNode *head)
    {
        while (head) {
            cout << head->val << " ";
            head = head->next;
        }
        cout << endl;
    }
};

} // namespace leetcode

#endif
