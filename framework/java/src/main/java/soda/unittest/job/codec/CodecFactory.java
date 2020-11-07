package soda.unittest.job.codec;

import java.util.HashMap;
import java.util.Map;

public class CodecFactory {
	
	private static Map<Class<?>, Class<? extends ICodec>> codecMap;
	
	static {
		codecMap = new HashMap<>();
		codecMap.put(int[].class, IntArrayCodec.class);
	}

	public static ICodec create(Class<?> objClass) {
		return new DefaultCodec();
	}
	
}
