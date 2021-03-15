import soda.unittest.*;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.work.TestWork;

import static soda.unittest.LoggerHelper.logger;

class CBTInserter {

    private ArrayDeque<TreeNode> qu = new ArrayDeque<>();

    private TreeNode root;

    public CBTInserter(TreeNode root) {
        this.root = root;
        qu.offerLast(root);
        while (!qu.isEmpty()) {
            var node = qu.peekFirst();
            if (node.left == null) {
                break;
            }
            qu.offerLast(node.left);
            if (node.right == null) {
                break;
            }
            qu.offerLast(node.right);
            qu.pollFirst();
        }
    }
    
    public int insert(int v) {
        var node = new TreeNode(v);
        var head = qu.peekFirst();
        qu.offerLast(node);
        if (head.left == null) {
            head.left = node;
        } else {
            head.right = node;
            qu.pollFirst();
        }
        return head.val;
    }
    
    public TreeNode get_root() {
        return root;
    }
}

class Solution {
    public List<Object> doTest(String[] commands, Object[] params) {
        List<Object> res = new ArrayList<>();
        CBTInserter cb = null;
        for (int i = 0; i < commands.length; ++i) {
            if (commands[i].equals("CBTInserter")) {
                var p = (List<List<Integer>>) params[i];
                var root = TreeFactory.create(p.get(0));
                cb = new CBTInserter(root);
                res.add(null);
            } else if (commands[i].equals("insert")) {
                var p = (List<Integer>) params[i];
                res.add(cb.insert(p.get(0)));
            } else {
                var root = cb.get_root();
                res.add(TreeFactory.dump(root));
            }
        }
        return res;
    }
}

public class Leet implements Supplier<TestWork> {

    @Override
    public TestWork get() {
        var work = new TestWork(new Solution(), "doTest");
        // work.setValidator((e, r) -> {...});
        work.setCompareSerial(true);
        // work.setArgumentParser(index, a -> { ... });
        // work.setResultParser(r -> { ... });
        // work.setResultSerializer(r -> {...});
        return work;
    }

    public static void main(String[] args) throws Exception {
        new Leet().get().run();
    }

}
