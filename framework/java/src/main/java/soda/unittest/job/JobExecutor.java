package soda.unittest.job;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

import com.fasterxml.jackson.databind.ObjectMapper;

import soda.unittest.job.codec.CodecFactory;
import soda.unittest.job.codec.ICodec;

public class JobExecutor {

	@SuppressWarnings("unchecked")
	public String exec(String input, JobSpec jspec) throws Exception {
		ObjectMapper json = new ObjectMapper();
		var inputData = json.readValue(input, InputData.class);
		
		Object[] args = new Object[jspec.argClasses.length];
		for (int i = 0; i < args.length; ++i) {
			ICodec codec = CodecFactory.create(jspec.argClasses[i]);
			args[i] = codec.decode(inputData.arg(i));
		}
		
		Constructor<?> ctor = jspec.jobClass.getDeclaredConstructor();
		ctor.setAccessible(true);
		Object solution = ctor.newInstance();
		Method method = jspec.method;
		method.setAccessible(true);
		
		long startNano = System.nanoTime();
		Object res = method.invoke(solution, args);
		long endNano = System.nanoTime();
		
		double elapseMillis = (endNano - startNano) / 1e6;
		Object serialRes = CodecFactory.create(jspec.retClass).encode(res);
		
		var outputData = new OutputData();
		outputData.id = inputData.id;
		outputData.result = serialRes;
		outputData.elapse = elapseMillis;
		
		boolean success = true;
		if (inputData.hasExpected()) {
			if (jspec.validateByObject) {
				Validator<?> vf = jspec.objectValidator;
				if (vf == null) {
					vf = new EqualValidator();
				}
				Object expectObject = CodecFactory.create(jspec.retClass).decode(inputData.expected);
				success = ((Validator<Object>)vf).validate(expectObject, res);
			} else {
				Validator<?> vf = jspec.serialValidator;
				if (vf == null) {
					vf = new EqualValidator();
				}
				success = ((Validator<Object>)vf).validate(inputData.expected, serialRes);
			}
		}
		
		outputData.success = success;
		return json.writeValueAsString(outputData);
	}
	
}
