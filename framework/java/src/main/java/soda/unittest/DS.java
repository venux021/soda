package soda.unittest;

import java.util.List;

@SuppressWarnings({ "unchecked", "rawtypes" })
public class DS {

	public static List<Integer> asIntList(Object obj) {
		return (List<Integer>) obj;
	}
	
	public static List<List<Integer>> asIntList2d(Object obj) {
		return (List<List<Integer>>) obj;
	}
	
}
