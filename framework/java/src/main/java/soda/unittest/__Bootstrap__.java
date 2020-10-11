package soda.unittest;

import java.util.*;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import soda.leetcode.*;

// step [1]: implement class Solution
// class Solution {}

// step [2]: implement test job
class TestJob extends JobTemplate<Object, Object> {

    public static Logger logger = LogManager.getLogger(TestJob.class);

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

} 

public class __Bootstrap__ {
    
    public static void main(String[] args) throws Exception {
        ObjectMapper json = new ObjectMapper();

        TestRequest req = json.readValue(readStdin(), TestRequest.class);
        TestResponse resp = new TestResponse();
        resp.id = req.id;
        
        TestJob job = new TestJob();

        long startNano = System.nanoTime();
        job.run(req, resp);
        long endNano = System.nanoTime();
        
        resp.elapse = (endNano - startNano) / 1e6;

        if (req.hasExpected()) {
            resp.success = job.validate(req, resp);
        } else {
            resp.success = true;
        }
        
        System.out.println(json.writeValueAsString(resp));
    }
    
    private static String readStdin() throws Exception {
        try (Scanner scan = new Scanner(System.in, "UTF-8")) {
            StringBuilder buf = new StringBuilder();
            while (scan.hasNextLine()) {
                buf.append(scan.nextLine());
            }   
            return buf.toString();
        }
    }
    
}
