package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class IntArray2dCodec implements ICodec {

	@Override
	public List<List<Integer>> encode(Object object) {
		return DataUtils.toList2d((int[][]) object);
	}

	@Override
	public int[][] decode(Object serial) {
		return DataUtils.toIntArray2d((List<?>) serial);
	}

}
