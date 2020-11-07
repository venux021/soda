package soda.unittest.job.codec;

import soda.unittest.DataUtils;

public class ObjectArrayCodec implements ICodec {
	
	private Class<?> elementType;
	
	private int dimensions;
	
	public ObjectArrayCodec(Class<?> elementType, int D) {
		this.elementType = elementType;
		dimensions = D;
	}

	@Override
	public Object encode(Object object) {
		return DataUtils.toList(object);
	}

	@Override
	public Object decode(Object serial) {
		return DataUtils.toArray(serial, elementType, dimensions);
	}

}
