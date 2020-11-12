package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class IntArray2dCodec implements ICodec<List<List<Integer>>, int[][]> {

	@Override
	public List<List<Integer>> encode(int[][] object) {
		return DataUtils.toList2d(object);
	}

	@Override
	public int[][] decode(List<List<Integer>> serial) {
		return DataUtils.toIntArray2d((List<?>) serial);
	}

}
