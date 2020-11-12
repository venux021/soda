package soda.unittest.job.codec;

public interface ICodec<_Serial, _Object> {

	_Serial encode(_Object object);
	
	_Object decode(_Serial serial);
	
}
