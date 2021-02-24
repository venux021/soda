package soda.unittest.work;

import java.io.IOException;

public class StringTestLoader implements TestLoader {
	
	private String input;
	
	private String output;
	
	public StringTestLoader(String content) {
		this.input = content;
	}

	@Override
	public String load() throws IOException {
		return input;
	}

	@Override
	public void store(String message) throws IOException {
		output = message;
	}
	
	public String getOutput() {
		return output;
	}

}
