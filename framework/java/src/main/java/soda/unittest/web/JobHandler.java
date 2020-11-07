package soda.unittest.web;

import java.lang.reflect.Constructor;
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpExchange;

import soda.unittest.JobRunner;
import soda.unittest.JobTemplate;
import soda.unittest.job.JobExecutor;
import soda.unittest.job.JobSpec;

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
		
		Callable<String> callable = null;
		if (JobTemplate.class.isAssignableFrom(klass)) {
	    	callable = () -> {
	    		Constructor<?> ctor = klass.getDeclaredConstructor();
				ctor.setAccessible(true);
				JobTemplate<?,?> job = (JobTemplate<?,?>) ctor.newInstance();
	    		JobRunner runner = new JobRunner();
	    		return runner.runJob(jr.request, job);
	    	};
		} else {
			callable = () -> {
				var spec = (JobSpec) klass.getMethod("createSpec").invoke(null);
				var executor = new JobExecutor();
				return executor.exec(jr.request, spec);
			};
		}
		
		TimeLimitedJob tLJob = new TimeLimitedJob(callable);
		FutureTask<String> future = tLJob.start();
    	try {
    		return future.get(timeoutMillis, TimeUnit.MILLISECONDS);
    	} catch (TimeoutException tex) {
    		tLJob.kill();
    		throw new RuntimeException("Job timeout");
    	}
	}

}
