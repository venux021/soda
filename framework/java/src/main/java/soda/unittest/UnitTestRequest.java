package soda.unittest;

import java.util.List;

public class UnitTestRequest {

	public int id;
	
	public Object answer;
	
	public List<Object> args;
	
	public <T> T arg(int index, Class<T> klass) {
		if (args != null && args.size() > index) {
			return klass.cast(args.get(index));
		}
		return null;
	}
	
}
