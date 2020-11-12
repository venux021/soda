package soda.unittest.job.codec;

public class DefaultCodec implements ICodec<Object, Object> {

	@Override
	public Object encode(Object object) {
		return object;
	}
	
	@Override
	public Object decode(Object serial) {
		return serial;
	}
	
}
