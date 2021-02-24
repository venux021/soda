package soda.unittest.work;

import java.io.IOException;

public interface TestLoader {

	String load() throws IOException;
	
	void store(String message) throws IOException;
	
}
