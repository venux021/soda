package soda.leetcode;

import java.util.List;

public class ListHelper {

	public static ListNode create(List<Integer> values) {
		return ListFactory.create(values);
	}
	
	public static List<Integer> dump(ListNode head) {
		return ListFactory.dump(head);
	}
	
	public static boolean isEqual(ListNode L1, ListNode L2) {
		while (L1 != null && L2 != null) {
			if (L1.val != L2.val) {
				return false;
			}
			L1 = L1.next;
			L2 = L2.next;
		}
		return L1 == null && L2 == null;
	}
	
}
