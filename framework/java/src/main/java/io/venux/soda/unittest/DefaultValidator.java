package io.venux.soda.unittest;

import java.lang.reflect.Array;
import java.util.List;

public class DefaultValidator implements ResultValidator {
	
	@Override
	public boolean validate(Object result, Object answer) {
		if (result == null) {
			return answer == null;
		}
		
		Class<?> cls = result.getClass();
		if (cls != answer.getClass()) {
			System.err.println("class type not match");
			return false;
		}
		
		if (cls.isArray()) {
			return validateArray(result, answer);
		}
		
		if (cls == List.class) {
			return validateList(result, answer);
		}
		
		return result.equals(answer);
	}
	
	@SuppressWarnings("rawtypes")
	private boolean validateList(Object result, Object answer) {
		List L1 = (List) result;
		List L2 = (List) answer;
		if (L1.size() != L2.size()) {
			return false;
		}
		for (int i = 0; i < L1.size(); ++i) {
			if (!validate(L1.get(i), L2.get(i))) {
				return false;
			}
		}
		return true;
	}
	
	private boolean validateArray(Object result, Object answer) {
		int length = Array.getLength(result);
		if (length != Array.getLength(answer)) {
			return false;
		}
		for (int i = 0; i < length; ++i) {
			Object a = Array.get(result, i);
			Object b = Array.get(answer, i);
			if (!validate(a, b)) {
				return false;
			}
		}
		return true;
	}

}
