package soda.unittest.job;

import java.lang.reflect.Method;

public class JobSpec {

	public Class<?> jobClass;
	
	public Method method;
	
	public Class<?> retClass;
	
	public Class<?>[] argClasses;
	
	public boolean validateByObject = false;
	
	public Validator<?> objectValidator;
	
	public Validator<?> serialValidator;
	
	public JobSpec(Class<?> jobClass, String method) throws NoSuchMethodException {
		this.jobClass = jobClass;
		this.method = findMethod(jobClass, method);
		retClass = this.method.getReturnType();
		argClasses = this.method.getParameterTypes();
	}
	
	private Method findMethod(Class<?> jobClass, String methodName) throws NoSuchMethodException {
		Method[] methods = jobClass.getMethods();
		for (Method m : methods) {
			if (m.getName().equals(methodName)) {
				return m;
			}
		}
		throw new NoSuchMethodException(methodName);
	}
	
}
