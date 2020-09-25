package soda.unittest;

public abstract class JobTemplate<Result, ResultSerial> {

	public void run(TestRequest req, TestResponse resp) {
		resp.setResult(serialize(execute(req, resp)));
	}
	
	public abstract Result execute(TestRequest req, TestResponse resp);
	
	public abstract ResultSerial serialize(Result res);
	
	public abstract boolean validate(TestRequest req, TestResponse resp);
	
}
