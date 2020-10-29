package soda.unittest;

import java.util.*;
import java.util.stream.*;

import soda.leetcode.*;

import static soda.unittest.LoggerHelper.logger;

// step [1]: implement class Solution
// class Solution {}

// step [2]: implement test job
public class __Bootstrap__ extends JobTemplate<Object, Object> {

    @Override
    public Object execute(TestRequest req, TestResponse resp) {
        // TODO
        throw new RuntimeException("Not implemented");
    }
    
    @Override
    public Object serialize(Object res) {
        return res;
    }
    
    @Override
    public boolean validate(TestRequest req, TestResponse resp) {
        return req.getExpected(Object.class).equals(resp.getResult(Object.class));
    }
    
    public static void main(String[] args) throws Exception {
        new ConsoleRunner().run(new __Bootstrap__());
    }

}
