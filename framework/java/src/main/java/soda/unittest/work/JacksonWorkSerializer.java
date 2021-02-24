package soda.unittest.work;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JacksonWorkSerializer implements WorkSerializer {
	
	private ObjectMapper json = new ObjectMapper();
	
	@Override
	public WorkInput parse(String str) {
		try {
			return json.readValue(str, WorkInput.class);
		} catch (JsonProcessingException ex) {
			throw new RuntimeException(ex);
		}
	}
	
	@Override
	public String serialize(WorkOutput output) {
		try {
			return json.writeValueAsString(output);
		} catch (JsonProcessingException ex) {
			throw new RuntimeException(ex);
		}
	}

}
