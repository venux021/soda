package soda.scala.unittest

import soda.unittest.LoggerHelper.logger

import soda.scala.unittest.job.AbstractScalaJob
import soda.scala.unittest.job.JobEntry
import soda.scala.unittest.job.JobSpec

// setp [1]: implement object Solution
object Solution {}

class __Bootstrap__ extends AbstractScalaJob {
    override def createSpec() = {
        // step [2]: setup job information
        val spec = new JobSpec(Solution.getClass, "METHOD")
        // do some configuration of spec
        spec
    }
}

object __Bootstrap__ extends App {
    JobEntry.run(new __Bootstrap__())
}
