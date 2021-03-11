package main

import . "soda/leetcode"
import "soda/unittest"

func reverse(head *ListNode) *ListNode {
    var h *ListNode = nil
    for head != nil {
        n := head.Next
        head.Next = h
        h = head
        head = n
    }
    return h
}

func validate(e *ListNode, r *ListNode) bool {
    for e != nil && r != nil {
        if e.Val != r.Val {
            return false
        }
        e = e.Next
        r = r.Next
    }
    return e == r
}

func main() {
    work := unittest.CreateWork(reverse)
    // work.SetValidator(validate)
    work.CompareSerial = true
    // work.SetArgParser(index, func(s)a)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
