import soda.unittest.*;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.work.TestWork;

import static soda.unittest.LoggerHelper.logger;

class Solution {
    public ListNode reverse(ListNode head) {
        ListNode h = null;
        while (head != null) {
            var n = head.next;
            head.next = h;
            h = head;
            head = n;
        }
        return h;
    }
}

public class TList implements Supplier<TestWork> {

    @Override
    public TestWork get() {
        var work = new TestWork(new Solution(), "reverse");
        work.setValidator((e, r) -> validate((ListNode) e, (ListNode) r));
        // work.setCompareSerial(true);
        // work.setArgumentParser(index, a -> { ... });
        // work.setResultParser(r -> { ... });
        // work.setResultSerializer(r -> {...});
        return work;
    }

    private boolean validate(ListNode e, ListNode r) {
        while (e != null && r != null) {
            if (e.val != r.val) {
                return false;
            }
            e = e.next;
            r = r.next;
        }
        return e == r;
    }

    public static void main(String[] args) throws Exception {
        new TList().get().run();
    }

}
