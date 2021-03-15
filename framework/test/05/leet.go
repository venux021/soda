package main

import "encoding/json"
import "fmt"

import . "soda/leetcode"
import "soda/unittest"
import "soda/util"

type CBTInserter struct {
    qu []*TreeNode
    root *TreeNode
}


func Constructor(root *TreeNode) CBTInserter {
    var cb CBTInserter
    cb.root = root
    cb.qu = append(cb.qu, root)
    for len(cb.qu) > 0 {
        node := cb.qu[0]
        if node.Left == nil {
            break
        }
        cb.qu = append(cb.qu, node.Left)
        if node.Right == nil {
            break
        }
        cb.qu = append(cb.qu, node.Right)
        cb.qu = cb.qu[1:]
    }
    return cb
}


func (this *CBTInserter) Insert(v int) int {
    node := new(TreeNode)
    node.Val = v
    head := this.qu[0]
    this.qu = append(this.qu, node)
    if head.Left == nil {
        head.Left = node
    } else {
        head.Right = node
        this.qu = this.qu[1:]
    }
    return head.Val
}


func (this *CBTInserter) Get_root() *TreeNode {
    return this.root
}

type InputData struct {
    root *TreeNode
    ops [][]int
}

func parseInputData(data []json.RawMessage) InputData {
    var input InputData
    var treeData []util.OptionalIntSlice
    if err := json.Unmarshal(data[0], &treeData); err != nil {
        panic(fmt.Sprintf("json parse error: %s\n", err))
    }
    input.root = TreeCreate(treeData[0])

    input.ops = append(input.ops, nil)
    for i := 1; i < len(data); i++ {
        var op []int
        if err := json.Unmarshal(data[i], &op); err != nil {
            panic(fmt.Sprintf("json parse error: %s\n", err))
        }
        input.ops = append(input.ops, op)
    }
    return input
}

func doTest(commands []string, input InputData) []interface{} {
    var res []interface{}
    var cb CBTInserter
    for i, cmd := range commands {
        if cmd == "CBTInserter" {
            cb = Constructor(input.root)
            res = append(res, nil)
        } else if cmd == "insert" {
            ins := cb.Insert(input.ops[i][0])
            res = append(res, ins)
        } else {
            root := cb.Get_root()
            res = append(res, TreeDump(root))
        }
    }
    return res
}

func main() {
    work := unittest.CreateWork(doTest)
    // work.SetValidator(func(e,r)bool)
    work.CompareSerial = true
    work.SetArgParser(1, parseInputData)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
