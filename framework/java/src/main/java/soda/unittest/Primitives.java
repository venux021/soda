package soda.unittest;

import java.util.HashMap;
import java.util.Map;

public class Primitives {

	private static Map<Class<?>, Class<?>> primToWrap = new HashMap<>();
	
	private static Map<Class<?>, Class<?>> wrapToPrim = new HashMap<>();
	
	private static void addPair(Class<?> primClass, Class<?> wrapClass) {
		primToWrap.put(primClass, wrapClass);
		wrapToPrim.put(wrapClass, primClass);
	}
	
	static {
		addPair(byte.class, Byte.class);
		addPair(char.class, Character.class);
		addPair(short.class, Short.class);
		addPair(int.class, Integer.class);
		addPair(long.class, Long.class);
		addPair(float.class, Float.class);
		addPair(double.class, Double.class);
		addPair(void.class, Void.class);
	}
	
	public static boolean isWrapperClass(Class<?> klass) {
		return wrapToPrim.containsKey(klass);
	}
	
	public static Class<?> getPrimitiveClass(Class<?> wrapClass) {
		return wrapToPrim.get(wrapClass);
	}
	
	public static Class<?> getWrapperClass(Class<?> primClass) {
		return primToWrap.get(primClass);
	}
	
}
