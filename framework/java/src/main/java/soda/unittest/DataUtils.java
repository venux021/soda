package soda.unittest;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@SuppressWarnings("unchecked")
public class DataUtils {
	
	public static <T> Object toPrimitiveArray(List<T> L, Class<T> wrapClass) {
		Class<?> primClass = Primitives.getPrimitiveClass(wrapClass);
		Object array = Array.newInstance(primClass, L.size());
		for (int i = 0; i < L.size(); ++i) {
			Array.set(array, i, L.get(i));
		}
		return array;
	}
	
	public static <W> List<W> fromPrimitiveArray(Object primArray, Class<W> wrapClass) {
		List<W> L = new ArrayList<>();
		for (int i = 0; i < Array.getLength(primArray); ++i) {
			L.add((W) Array.get(primArray, i));
		}
		return L;
	}
	
	public static <T> T[] toArray(List<T> L, Class<T> klass) {
		T[] array = (T[]) Array.newInstance(klass, L.size());
		L.toArray(array);
		return array;
	}
	
	public static <T> List<T> toList(T[] array) {
		return Arrays.asList(array);
	}
	
	public static <T> Object toPrimitiveArray2d(List<List<T>> L, Class<T> wrapClass) {
		int d1 = L.size(), d2 = 0;
		if (d1 > 0) {
			d2 = L.get(0).size();
		}
		Class<?> primClass = Primitives.getPrimitiveClass(wrapClass);
		Object array = Array.newInstance(primClass, d1, d2);
		for (int i = 0; i < d1; ++i) {
			Object a = Array.get(array, i);
			for (int j = 0; j < d2; ++j) {
				Array.set(a, j, L.get(i).get(j));
			}
		}
		return array;
	}
	
	public static <T> List<List<T>> fromPrimitiveArray2d(Object primArray2d, Class<T> wrapClass) {
		List<List<T>> L = new ArrayList<>();
		for (int i = 0; i < Array.getLength(primArray2d); ++i) {
			Object arr = Array.get(primArray2d, i);
			List<T> L2 = new ArrayList<>();
			for (int j = 0; j < Array.getLength(arr); ++j) {
				L2.add((T) Array.get(arr, j));
			}
			L.add(L2);
		}
		return L;
	}
	
	public static <T> T[][] toArray2d(List<List<T>> L, Class<T> klass) {
		int d1 = L.size(), d2 = 0;
		if (d1 > 0) {
			d2 = L.get(0).size();
		}
		T[][] array2d = (T[][]) Array.newInstance(klass, d1, d2);
		for (int i = 0; i < d1; ++i) {
			L.get(i).toArray(array2d[i]);
		}
		return array2d;
	}
	
	public static <T> List<List<T>> toList2d(T[][] array2d) {
		List<List<T>> L = new ArrayList<>();
		for (T[] arr : array2d) {
			L.add(toList(arr));
		}
		return L;
	}
	
	public static void main(String[] args) {
		int[][] arr2d = new int[][] {{1,2,3}, {4,5,6}, {7,8,9}};
		List<List<Integer>> L = fromPrimitiveArray2d(arr2d, Integer.class);
		int[][] arr2d1 = (int[][]) toPrimitiveArray2d(L, Integer.class);
		for (int i = 0; i < arr2d1.length; ++i) {
			for (int j = 0; j < arr2d1[i].length; ++j) {
				System.out.print(arr2d1[i][j] + " ");
			}
			System.out.println();
		}
		
//		List<Integer> L1 = new ArrayList<>();
//		L1.add(1); L1.add(2); L1.add(3);
//		int[] arr1 = (int[]) toPrimitiveArray(L1, Integer.class);
//		for (int i = 0; i < L1.size(); ++i) {
//			System.out.println(arr1[i]);
//		}
//		System.out.println(fromPrimitiveArray(arr1, Integer.class));
		
	}
	
}
