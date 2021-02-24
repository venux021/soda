package soda.unittest.work;

public interface WorkSerializer {

	WorkInput parse(String str);
	
	String serialize(WorkOutput output);
	
}
