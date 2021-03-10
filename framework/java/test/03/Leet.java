import soda.unittest.*;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.work.TestWork;

import static soda.unittest.LoggerHelper.logger;

class Input1 {
    public int value;
    public Input1(int value) {
        this.value = value;
    }
}

class Input2 {
    public String text;
    public Input2(String text) {
        this.text = text;
    }
}

class Output {
    public int val;
    public String str;
    Output(int val, String str) {
        this.val = val;
        this.str = str;
    }
}

class Solution {
    public Output gen(Input1 i1, Input2 i2) {
        return new Output(i1.value, i2.text);
    }
}

public class Leet implements Supplier<TestWork> {

    @Override
    public TestWork get() {
        var work = new TestWork(new Solution(), "gen");
        // work.setValidator((e, r) -> {...});
        work.setValidator((Output v1, Output v2) ->
                v1.val == v2.val && (v1.str == v2.str || v1.str != null && v1.str.equals(v2.str)));
        // work.setCompareSerial(true);
        // work.setArgumentParser(index, a -> { ... });
        work.setArgumentParser(0, (Integer v) -> new Input1(v));
        work.setArgumentParser(1, (String v) -> new Input2(v));
        // work.setResultParser(r -> { ... });
        work.setResultParser((List<String> v) -> new Output(v.size(), v.get(0)));
        // work.setResultSerializer(r -> {...});
        work.setResultSerializer((Output v) -> {
            String[] s = new String[v.val];
            for (int i = 0; i < v.val; ++i) {
                s[i] = v.str;
            }
            return s;
        });
        return work;
    }

    public static void main(String[] args) throws Exception {
        new Leet().get().run();
    }

}
