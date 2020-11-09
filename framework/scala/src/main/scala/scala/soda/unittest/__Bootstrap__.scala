package scala.soda.unittest

import java.util._
import java.util.stream._

import soda.leetcode._
import soda.unittest.job.JobEntry
import soda.unittest.job.JobSpec

import soda.unittest.LoggerHelper.logger

// setp [1]: implement object Solution
object Solution {}

object __Bootstrap__ {
    def createSpec() = {
        // step [2]: setup job information
        val spec = new JobSpec(Solution.getClass, "METHOD")
        // do some configuration of spec
        spec
    }
    def main(args: Array[String]): Unit = JobEntry.run(createSpec())
}
