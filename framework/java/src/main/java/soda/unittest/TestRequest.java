package soda.unittest;

import java.util.List;

public class TestRequest {

	public int id;
	
	public Object expected;
	
	public List<Object> args;
	
	public <T> T arg(int index, Class<T> klass) {
		if (args != null && args.size() > index) {
			return klass.cast(args.get(index));
		}
		return null;
	}
	
	public Object arg(int index) {
		return args != null && args.size() > index ? args.get(index) : null;
	}
	
	public boolean hasExpected() {
		return expected != null;
	}
	
	public <T> T getExpected(Class<T> klass) {
		return klass.cast(expected);
	}
	
}
