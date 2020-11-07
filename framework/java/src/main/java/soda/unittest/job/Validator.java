package soda.unittest.job;

public interface Validator<T> {

	boolean validate(T expect, T result);
	
}
