package soda.unittest;

import java.util.Scanner;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Runner {
    
    public void run(JobTemplate<?,?> job) throws Exception {
        ObjectMapper json = new ObjectMapper();

        TestRequest req = json.readValue(readStdin(), TestRequest.class);
        TestResponse resp = new TestResponse();
        resp.id = req.id;
        
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
