package soda.unittest;

import com.fasterxml.jackson.databind.ObjectMapper;

public class JobRunner {

	public String runJob(String input, JobTemplate<?,?> job) throws Exception {
		ObjectMapper json = new ObjectMapper();

        TestRequest req = json.readValue(input, TestRequest.class);
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
        
        return json.writeValueAsString(resp);
	}
	
}
