package soda.unittest.job;

public class EqualValidator implements Validator<Object> {

	public boolean validate(Object expect, Object result) {
		return expect != null ? expect.equals(result) : result == null;
	}
	
}
