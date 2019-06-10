#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
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
