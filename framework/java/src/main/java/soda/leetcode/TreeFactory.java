package soda.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class TreeFactory {

	public static TreeNode create(List<Integer> treeData) {
		if (treeData.size() == 0) {
			return null;
		}
		
		TreeNode root = new TreeNode(treeData.get(0));
		Deque<TreeNode> qu = new ArrayDeque<>();
		qu.offerLast(root);
		for (int i = 1; i < treeData.size(); ) {
			var node = qu.pollFirst();
			if (treeData.get(i) != null) {
				node.left = new TreeNode(treeData.get(i));
				qu.offerLast(node.left);
			}
			++i;
			if (i == treeData.size()) {
				break;
			}
			if (treeData.get(i) != null) {
				node.right = new TreeNode(treeData.get(i));
				qu.offerLast(node.right);
			}
			++i;
		}
		return root;
	}
	
	public static List<Integer> dump(TreeNode root) {
		List<Integer> data = new ArrayList<>();
		if (root == null) {
			return data;
		}
		
		List<TreeNode> curr = new ArrayList<>(), next = new ArrayList<>(), order = new ArrayList<>();
		curr.add(root);
		while (curr.size() > 0) {
			next.clear();
			for (TreeNode node : curr) {
				order.add(node);
				if (node != null) {
					next.add(node.left);
					next.add(node.right);
				}
			}
			var temp = curr;
			curr = next;
			next = temp;
		}
		
		int i = order.size() - 1;
		while (order.get(i) == null) {
			--i;
		}
		for (int j = 0; j <= i; ++j) {
			if (order.get(j) != null) {
				data.add(order.get(j).val);
			} else {
				data.add(null);
			}
		}
		return data;
	}
	
}
