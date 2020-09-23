package soda.unittest;

import java.util.List;

import soda.leetcode.ListHelper;
import soda.leetcode.ListNode;

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
	
	public Object arg(int index) {
		return args != null && args.size() > index ? args.get(index) : null;
	}
	
	public ListNode argLinkList(int index) {
		return ListHelper.create(DS.asIntList(arg(index)));
	}
	
}
