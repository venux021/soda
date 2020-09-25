package soda.unittest;

public class TestResponse {

	public int id;
	
	public boolean success;
	
	public Object result;
	
	public double elapse;
	
	public void setResult(Object res) {
		this.result = res;
	}
	
	public <T> T getResult(Class<T> klass) {
		return klass.cast(result);
	}
	
}
