package soda.leetcode;

import java.util.ArrayList;
import java.util.List;

public class ListFactory {
	
	public static ListNode create(List<Integer> values) {
		ListNode head = new ListNode(-1);
		ListNode tail = head;
		for (int value : values) {
			ListNode node = new ListNode(value);
			tail.next = node;
			tail = node;
		}
		return head.next;
	}
	
	public static List<Integer> dump(ListNode head) {
		List<Integer> list = new ArrayList<>();
		while (head != null) {
			list.add(head.val);
			head = head.next;
		}
		return list;
	}
	
}
