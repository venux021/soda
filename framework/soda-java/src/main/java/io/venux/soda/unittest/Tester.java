package io.venux.soda.unittest;

import java.io.BufferedReader;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Tester {
	
	public static final String DEFAULT_INPUT_FILE = "input.txt";
	
	private Class<?> resultClass;

	private Class<?>[] inputClasses;

	private int testCount;

	private ObjectMapper objectMapper = new ObjectMapper();
	
	public ResultValidator validator = new DefaultValidator();
	
	private Object worker;
	
	private Method method;

	public Tester(Class<?> resultClass, Class<?>... inputClasses) {
		this.resultClass = resultClass;
		this.inputClasses = inputClasses;
	}
	
	private static class DefaultValidator implements ResultValidator {
		
		@Override
		public boolean validate(Object result, Object answer) {
			return result != null ? result.equals(answer) : answer == null;
		}
		
	}
	
	public void all(Object worker, String methodName) {
		all(worker, methodName, DEFAULT_INPUT_FILE);
	}
	
	public void all(Object worker, String methodName, String inputFile) {
		all(worker, methodName, new String[] { inputFile });
	}

	public void all(Object worker, String methodName, String... inputFiles) throws RuntimeException {
		try {
			this.worker = worker;
			method = worker.getClass().getMethod(methodName, this.inputClasses);
			
			int numArgs = inputClasses.length;
			List<String> lines = new ArrayList<>();
			TestAttribute ta = new TestAttribute();
			
			for (String inputFile : inputFiles) {
				try (BufferedReader reader = Files.newBufferedReader(Paths.get(inputFile), StandardCharsets.UTF_8)) {
					String line = null;
					while ((line = reader.readLine()) != null) {
						line = line.trim();
						if (line.length() > 2 && line.substring(0, 2).equals("#$")) {
							ta = parseTestAttribute(line);
						} else if (line.length() == 0 || line.charAt(0) == '#') {
							continue;
						} else {
							lines.add(line);
							if (lines.size() > numArgs) {
								doExecute(lines, ta);
								lines.clear();
								ta = new TestAttribute();
							}
						}
					}
				}
			}
		} catch (Exception ex) {
			throw new RuntimeException(ex);
		}
	}
	
	private void doExecute(List<String> lines, TestAttribute ta) throws Exception {
		int numArgs = inputClasses.length;
		Object[] args = new Object[numArgs];
		for (int i = 0; i < numArgs; ++i) {
			args[i] = objectMapper.readValue(lines.get(i), inputClasses[i]);
		}
		
		Object answer = null;
		String last = lines.get(lines.size() - 1);
		if (!last.equals("null")) {
			answer = objectMapper.readValue(last, resultClass);
		}
		execute(args, answer, ta);
	}
	
	private TestAttribute parseTestAttribute(String line) {
		String[] attrs = line.substring(2).split(";");
		TestAttribute ta = new TestAttribute();
		for (String attr : attrs) {
			String[] keyValue = attr.split("=");
			String key = keyValue[0].trim();
			String value = keyValue[1].trim();
			if (key.equals("showArgs")) {
				ta.showArgs = value.equals("true");
			} else if (key.equals("skip")) {
				ta.skip = value.equals("true");
			} else if (key.equals("showResult")) {
				ta.showResult = value.equals("true");
			}
		}
		return ta;
	}

	private Object execute(Object[] args, Object answer, TestAttribute ta) throws Exception {
		System.out.printf("**[%d]**\n", ++testCount);

		if (ta.showArgs) {
			showArgs(args);
		}

		if (ta.skip) {
			return null;
		}

		long startNano = System.nanoTime();
		Object res = method.invoke(worker, args);
		long endNano = System.nanoTime();
		
		if (answer != null && !validator.validate(res, answer)) {
			throw new RuntimeException(String.format("Wrong answer %s, but %s expected", res, answer));
		}
		
		if (ta.showResult) {
			showResult(res);
		}
		
		System.out.println("----");
		System.out.printf("%.2fms\n\n", (endNano - startNano) / 1e6);
		
		return res;
	}
	
	private void showResult(Object res) {
		System.out.println("output:\n" + res);
	}

	private void showArgs(Object[] args) {
		System.out.println("input:");
		for (int i = 0; i < args.length; ++i) {
			Object arg = args[i];
			String str = null;
			if (arg.getClass().isArray()) {
				try {
					str = objectMapper.writeValueAsString(arg);
				} catch (JsonProcessingException e) {
					str = String.format("<not json serializable: %s, %s>", arg.getClass(), arg.toString());
				}
			} else {
				str = arg.toString();
			}
			System.out.print(str);
			if (i < args.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.println();
	}

}
