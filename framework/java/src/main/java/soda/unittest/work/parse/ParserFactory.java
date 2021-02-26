package soda.unittest.work.parse;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

import soda.leetcode.ListHelper;
import soda.leetcode.ListNode;
import soda.leetcode.TreeFactory;
import soda.leetcode.TreeNode;
import soda.unittest.job.codec.CodecFactory;
import soda.unittest.job.codec.ICodec;

public class ParserFactory {
	
	private static Map<Class<?>, Function<?,?>> parserMap;
	
	private static Map<Class<?>, Function<?,?>> serialMap;
	
	static {
		parserMap = new HashMap<>();
		serialMap = new HashMap<>();
		
		parserMap.put(ListNode.class, (List<Integer> L) -> ListHelper.create(L));
		serialMap.put(ListNode.class, (ListNode head) -> ListHelper.dump(head));
		
		parserMap.put(TreeNode.class, (List<Integer> L) -> TreeFactory.create(L));
		serialMap.put(TreeNode.class, (TreeNode root) -> TreeFactory.dump(root));
	}

	@SuppressWarnings("unchecked")
	public static Function<?,?> createParser(Class<?> klass) throws Exception {
		Function<?,?> parser = parserMap.get(klass);
		if (parser == null) {
			ICodec<Object,Object> codec = (ICodec<Object,Object>) CodecFactory.create(klass);
			parser = (Object obj) -> { return codec.decode(obj); };
		}
		return parser;
	}
	
	@SuppressWarnings("unchecked")
	public static Function<?,?> createSerializer(Class<?> klass) throws Exception {
		Function<?,?> parser = serialMap.get(klass);
		if (parser == null) {
			ICodec<Object,Object> codec = (ICodec<Object,Object>) CodecFactory.create(klass);
			parser = (Object obj) -> { return codec.encode(obj); };
		}
		return parser;
	}
	
}
