package soda.unittest.web;

import java.lang.reflect.Constructor;
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.function.Supplier;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpExchange;

import soda.unittest.AbstractTestJob;
import soda.unittest.CommonJob;
import soda.unittest.JobRunner;
import soda.unittest.JobTemplate;
import soda.unittest.job.JobExecutor;
import soda.unittest.job.JobSpec;
import soda.unittest.work.StringTestLoader;
import soda.unittest.work.TestWork;

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
		if (CommonJob.class.isAssignableFrom(klass)) {
			callable = () -> {
				Constructor<?> ctor = klass.getDeclaredConstructor();
				ctor.setAccessible(true);
				CommonJob cj = (CommonJob) ctor.newInstance();
				return cj.execute(jr.request);
			};
		} else if (JobTemplate.class.isAssignableFrom(klass)) {
	    	callable = () -> {
	    		Constructor<?> ctor = klass.getDeclaredConstructor();
				ctor.setAccessible(true);
				JobTemplate<?,?> job = (JobTemplate<?,?>) ctor.newInstance();
	    		JobRunner runner = new JobRunner();
	    		return runner.runJob(jr.request, job);
	    	};
		} else if (AbstractTestJob.class.isAssignableFrom(klass)) {
			callable = () -> {
				var spec = (JobSpec) klass.getMethod("createSpec").invoke(null);
				var executor = new JobExecutor();
				return executor.exec(jr.request, spec);
			};
		} else {
			callable = () -> {
				Constructor<?> ctor = klass.getDeclaredConstructor();
			    ctor.setAccessible(true);
			    var workDef = ctor.newInstance();
			    @SuppressWarnings("unchecked")
				TestWork work = ((Supplier<TestWork>)workDef).get();
			    StringTestLoader testLoader = new StringTestLoader(jr.request);
			    work.setTestLoader(testLoader);
			    work.run();
			    return testLoader.getOutput();
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
