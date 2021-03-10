import soda.unittest.*;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.work.TestWork;

import static soda.unittest.LoggerHelper.logger;

class TopVotedCandidate {

    int N = 0;
    int[] times;
    int[] winner;

    public TopVotedCandidate(int[] persons, int[] times) {
        N = persons.length;
        this.times = times;
        winner = new int[N];

        int[] counter = new int[N+1];
        int win = 0;
        for (int i = 0; i < N; ++i) {
            if (++counter[persons[i]] >= counter[win]) {
                win = persons[i];
            }
            winner[i] = win;
        }
    }
    
    public int q(int t) {
        if (t >= times[N-1]) {
            return winner[N-1];
        }
        int low = 0, high = N-1;
        while (low < high) {
            int mid = (low + high) / 2;
            if (t <= times[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return t == times[low] ? winner[low] : winner[low-1];
    }
}

class Params {
    public int[] persons;
    public int[] times;
    public int[] qs;
}

class Solution {
    public List<Integer> doTest(String[] commands, Params params) {
        List<Integer> res = new ArrayList<>();
        TopVotedCandidate tvc = null;
        for (int i = 0; i < commands.length; ++i) {
            if (commands[i].equals("TopVotedCandidate")) {
                tvc = new TopVotedCandidate(params.persons, params.times);
                res.add(null);
            } else {
                res.add(tvc.q(params.qs[i]));
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
        work.setArgumentParser(1, (List<Object> v) -> {
            Params params = new Params();
            var p0 = (List<List<Integer>>) v.get(0);
            params.persons = DataUtils.toIntArray(p0.get(0));
            params.times = DataUtils.toIntArray(p0.get(1));
            params.qs = new int[params.persons.length];
            for (int i = 1; i < v.size(); ++i) {
                List<Integer> p = (List<Integer>) v.get(i);
                params.qs[i] = p.get(0);
            }
            return params;
        });
        // work.setResultParser(r -> { ... });
        // work.setResultSerializer(r -> {...});
        return work;
    }

    public static void main(String[] args) throws Exception {
        new Leet().get().run();
    }

}
