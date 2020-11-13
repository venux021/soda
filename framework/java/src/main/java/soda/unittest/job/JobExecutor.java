package soda.unittest.job;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

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
			ICodec<Object,Object> codec = (ICodec<Object,Object>) CodecFactory.create(jspec.argClasses[i]);
			args[i] = codec.decode(inputData.arg(i));
		}
		
		Object solution = null;
		Method method = jspec.method;
		method.setAccessible(true);
        if (!Modifier.isStatic(method.getModifiers())) {
		    Constructor<?> ctor = jspec.jobClass.getDeclaredConstructor();
		    ctor.setAccessible(true);
		    solution = ctor.newInstance();
        }
		
		long startNano = System.nanoTime();
		Object res = method.invoke(solution, args);
		long endNano = System.nanoTime();
		
		double elapseMillis = (endNano - startNano) / 1e6;
		Object serialRes = ((ICodec<Object,Object>) CodecFactory.create(jspec.retClass)).encode(res);
		
		var outputData = new OutputData();
		outputData.id = inputData.id;
		outputData.result = serialRes;
		outputData.elapse = elapseMillis;
		
		boolean success = true;
		if (inputData.hasExpected()) {
			if (jspec.validateByObject) {
				Validator<?> vf = jspec.objectValidator;
				Object expectObject = ((ICodec<Object,Object>)CodecFactory.create(jspec.retClass)).decode(inputData.expected);
				success = ((Validator<Object>)vf).validate(expectObject, res);
			} else {
				Validator<?> vf = jspec.serialValidator;
				success = ((Validator<Object>)vf).validate(inputData.expected, serialRes);
			}
		}
		
		outputData.success = success;
		return json.writeValueAsString(outputData);
	}
	
}
