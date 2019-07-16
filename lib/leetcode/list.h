#ifndef _LEETCODE_LIST
#define _LEETCODE_LIST

namespace leetcode {

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

} // namespace leetcode

#endif
