package soda.unittest.job;

public class JobContext {

	public JobSpec spec;
	
	public Object[] args;
	
	public static JobContext current() {
		return jcLocal.get();
	}
	
	private static ThreadLocal<JobContext> jcLocal = new ThreadLocal<>();
	
	static void set(JobContext ctx) {
		jcLocal.set(ctx);
	}
	
}
