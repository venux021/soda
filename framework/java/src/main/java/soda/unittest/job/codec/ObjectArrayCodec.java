package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class ObjectArrayCodec implements ICodec<List<?>, Object> {
	
	private Class<?> elementType;
	
	private int dimensions;
	
	public ObjectArrayCodec(Class<?> elementType, int D) {
		this.elementType = elementType;
		dimensions = D;
	}

	@Override
	public List<?> encode(Object object) {
		return (List<?>) DataUtils.toList(object);
	}

	@Override
	public Object decode(List<?> serial) {
		return DataUtils.toArray(serial, elementType, dimensions);
	}

}
