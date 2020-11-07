package soda.unittest.job;

import soda.unittest.ConsoleRunner;

public class JobEntry {
	
	public static void run(Class<?> mainClass) throws Exception {
		JobDesc desc = mainClass.getAnnotation(JobDesc.class);
		run(desc.jobClass(), desc.method());
	}

	public static void run(Class<?> jobclass, String method) throws Exception {
		run(jobclass, method, false, null, null);
	}
	
	public static void runWithObjectCheck(
			Class<?> jobclass, String method, Validator<?> objectValidator) throws Exception 
	{
		run(jobclass, method, true, objectValidator, null);
	}
	
	public static void runWithSerialCheck(
			Class<?> jobclass, String method, Validator<?> serialValidator) throws Exception 
	{
		run(jobclass, method, false, null, serialValidator);
	}
	
	public static void run(
			Class<?> jobclass, String method, boolean validateByObject,
			Validator<?> objectValidator, Validator<?> serialValidator) throws Exception 
	{
		var jspec = new JobSpec(jobclass, method);
		new ConsoleRunner().run(jspec, new JobExecutor());
	}
	
}
