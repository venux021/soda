package soda.unittest.job.codec;

public class DefaultCodec implements ICodec {

	public Object encode(Object object) {
		return object;
	}
	
	public Object decode(Object serial) {
		return serial;
	}
	
}
