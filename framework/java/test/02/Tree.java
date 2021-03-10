import soda.unittest.*;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.work.TestWork;

import static soda.unittest.LoggerHelper.logger;

class Solution {
    public TreeNode mirror(TreeNode root) {
        if (root == null) {
            return null;
        }
        mirror(root.left);
        mirror(root.right);
        var temp = root.left;
        root.left = root.right;
        root.right = temp;
        return root;
    }
}

public class Tree implements Supplier<TestWork> {

    @Override
    public TestWork get() {
        var work = new TestWork(new Solution(), "mirror");
        work.setValidator((e, r) -> validate((TreeNode) e, (TreeNode) r));
        // work.setCompareSerial(true);
        // work.setArgumentParser(index, a -> { ... });
        // work.setResultParser(r -> { ... });
        // work.setResultSerializer(r -> {...});
        return work;
    }

    boolean validate(TreeNode e, TreeNode r) {
        if (e == null && r == null) {
            return true;
        } else if (e != null && r != null) {
            return e.val == r.val && validate(e.left, r.left) && validate(e.right, r.right);
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        new Tree().get().run();
    }

}
