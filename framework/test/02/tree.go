package main

import . "soda/leetcode"
import "soda/unittest"

func mirror(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    mirror(root.Left)
    mirror(root.Right)
    root.Left, root.Right = root.Right, root.Left
    return root
}

func validate(e, r *TreeNode) bool {
    if e == nil && r == nil {
        return true
    } else if e != nil && r != nil {
        return e.Val == r.Val && validate(e.Left, r.Left) && validate(e.Right, r.Right)
    }
    return false
}

func main() {
    work := unittest.CreateWork(mirror)
    work.SetValidator(validate)
    // work.CompareSerial = true
    // work.SetArgParser(index, func(s)a)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
