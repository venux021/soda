package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class IntArrayCodec implements ICodec<List<Integer>, int[]> {

	@Override
	public List<Integer> encode(int[] object) {
		return DataUtils.toList(object);
	}
	
	@Override
	public int[] decode(List<Integer> serial) {
		return DataUtils.toIntArray(serial);
	}
	
}
