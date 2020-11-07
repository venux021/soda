package soda.unittest.job.codec;

public interface ICodec {

	Object encode(Object object);
	
	Object decode(Object serial);
	
}
