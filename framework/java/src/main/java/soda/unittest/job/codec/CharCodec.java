package soda.unittest.job.codec;

import java.util.List;

import soda.unittest.DataUtils;

public class CharCodec implements ICodec<String, Character> {

	@Override
	public String encode(Character object) {
        return String.valueOf(object);
	}
	
	@Override
	public Character decode(String serial) {
        return serial.charAt(0);
	}
	
}
