package soda.unittest;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

import com.fasterxml.jackson.databind.ObjectMapper;

// step [0]: implement class Solution
// class Solution {}

public class __Bootstrap__ {
	
    // step [1]: implement validate function
	public static boolean validate(Object res, Object answer) {
		return res != null ? res.equals(answer) : answer == null;
	}

	public static void main(String[] args) throws Exception {
		ObjectMapper json = new ObjectMapper();
		String input = loadStdin();
		UnitTestRequest req = json.readValue(input, UnitTestRequest.class);
		
        // step [2]: deserialize arguments
		// arg1 = req.arg(index, <type>.class);
		
        // it's a little slow to load class Solution, so put it before time range
		Solution su = new Solution();
		long startNano = System.nanoTime();
		
        // step [3]: invoke solution function
        // res = su.someMethod(arg0, arg1, ...);
		
		long endNano = System.nanoTime();
		
		UnitTestResponse resp = new UnitTestResponse();
		resp.id = req.id;
		resp.elapse = (endNano - startNano) / 1e6;

        if (req.answer != null) {
            // step [4]: deserialize answer object if necessary
            resp.success = validate(res, req.answer);
        } else {
            resp.success = true;
        }

        // step [5]: serialize result object if necessary
		resp.result = res;
		
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
