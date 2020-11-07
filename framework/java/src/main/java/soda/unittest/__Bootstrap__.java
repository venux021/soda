package soda.unittest;

import java.util.*;
import java.util.stream.*;

import soda.leetcode.*;
import soda.unittest.job.JobEntry;
import soda.unittest.job.JobSpec;

import static soda.unittest.LoggerHelper.logger;

// step [1]: implement class Solution
class Solution {}

public class __Bootstrap__ {

    public static JobSpec createSpec() throws Exception {
        // step [2]: setup job information
        var spec = new JobSpec(Solution.class, "METHOD");
        // do some configuration of spec
        return spec;
    }

    public static void main(String[] args) throws Exception {
         JobEntry.run(createSpec());
    }
}
