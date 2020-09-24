package soda.unittest;

import java.util.List;

@SuppressWarnings("unchecked")
public class ArgReader {

	private UnitTestRequest req;
	
	public ArgReader(UnitTestRequest req) {
		this.req = req;
	}
	
	public int asInt(int index) {
		return req.arg(index, Integer.class);
	}
	
	public List<Integer> asIntList(int index) {
		return (List<Integer>) req.arg(index, List.class);
	}
	
	public List<List<Integer>> asIntList2d(int index) {
		return (List<List<Integer>>) req.arg(index, List.class);
	}
	
}
