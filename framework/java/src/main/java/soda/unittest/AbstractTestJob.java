package soda.unittest;

import soda.unittest.job.JobExecutor;
import soda.unittest.job.JobSpec;

public abstract class AbstractTestJob implements CommonJob {
	
	public abstract JobSpec createSpec() throws Exception;

	@Override
	public String execute(String input) throws Exception {
		JobExecutor je = new JobExecutor();
		return je.exec(input, createSpec());
	}

}
