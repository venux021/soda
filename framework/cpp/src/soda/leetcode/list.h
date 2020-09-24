#ifndef _SODA_LEETCODE_LIST_H_
#define _SODA_LEETCODE_LIST_H_

#include <vector>

namespace soda::leetcode {

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

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
