package soda.unittest.web;

import java.lang.reflect.Constructor;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpExchange;

import soda.unittest.JobRunner;
import soda.unittest.JobTemplate;

public class JobHandler extends BaseHandler {
	
	private final ClassLoaderManager mgr;
	
	private final long timeoutMillis;
	
	public JobHandler(ClassLoaderManager mgr, long timeoutMillis) {
		this.mgr = mgr;
		this.timeoutMillis = timeoutMillis;
	}

	@Override
	protected String handleJob(HttpExchange exchange) throws Exception {
		String content = getPostBody(exchange);
		ObjectMapper om = new ObjectMapper();
		JobRequest jr = om.readValue(content, JobRequest.class);
		
		ClassLoader loader = mgr.get(jr.runpath);
		Class<?> klass = loader.loadClass(jr.jobclass);
		Constructor<?> ctor = klass.getDeclaredConstructor();
		ctor.setAccessible(true);
		JobTemplate<?,?> job = (JobTemplate<?,?>) ctor.newInstance();
		
    	TimeLimitedJob tlJob = new TimeLimitedJob(() -> {
    		JobRunner runner = new JobRunner();
    		return runner.runJob(jr.request, job);
    	});
    	FutureTask<String> future = tlJob.start();
    	
    	try {
    		return future.get(timeoutMillis, TimeUnit.MILLISECONDS);
    	} catch (TimeoutException tex) {
    		tlJob.kill();
    		throw new RuntimeException("Job timeout");
    	}
	}

}
