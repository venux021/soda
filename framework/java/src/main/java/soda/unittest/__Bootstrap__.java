package soda.unittest;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

import com.fasterxml.jackson.databind.ObjectMapper;

public class __Bootstrap__ {
	
	public static boolean validate(Object res, Object answer) {
		return res != null ? res.equals(answer) : answer == null;
	}

	public static void main(String[] args) throws Exception {
		ObjectMapper json = new ObjectMapper();
		String input = loadStdin();
		UnitTestRequest req = json.readValue(input, UnitTestRequest.class);
		
		// get arg from req
		// arg1 = req.arg(index, <type>.class);
		
		long startNano = System.nanoTime();
		
		// TODO invoke Solution
		// Solution su = new Solution()
		// res = su.someMethod(arg1, arg2);
		Object res = null;
		
		long endNano = System.nanoTime();
		
		boolean success = req.answer == null || validate(res, req.answer);
		
		UnitTestResponse resp = new UnitTestResponse();
		resp.id = req.id;
		resp.success = success;
		resp.result = res;
		resp.elapse = (endNano - startNano) / 1e6;
		
		System.out.println(json.writeValueAsString(resp));
	}
	
	private static String loadStdin() throws Exception {
		try (InputStreamReader in = new InputStreamReader(System.in, StandardCharsets.UTF_8);
				BufferedReader reader = new BufferedReader(in)) {
			StringBuilder buf = new StringBuilder();
			String line = null;
			while ((line = reader.readLine()) != null) {
				buf.append(line);
			}
			return buf.toString();
		}
	}
	
}
