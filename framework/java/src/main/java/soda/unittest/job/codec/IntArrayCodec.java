package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class IntArrayCodec implements ICodec {

	public Object encode(Object object) {
		return DataUtils.toList((int[]) object);
	}
	
	public Object decode(Object serial) {
		return DataUtils.toIntArray((List<?>) serial);
	}
	
}
