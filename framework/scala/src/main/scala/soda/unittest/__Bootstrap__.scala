package soda.unittest

import java.util._
import java.util.stream._

import soda.leetcode._

import soda.unittest.LoggerHelper.logger

// setp [1]: implement object Solution
// object Solution

// step [2]: implement test job
class __Bootstrap__ extends JobTemplate[Object, Object] {

    override def execute(req: TestRequest, resp: TestResponse): Object = {
        // TODO
        throw new RuntimeException("Not implemented");
    }

    override def serialize(res: Object): Object = {
        res
    }
    
    override def validate(req: TestRequest, resp: TestResponse): Boolean = {
        req.getExpected(classOf[Object]).equals(resp.getResult(classOf[Object]))
    }

}

object __Bootstrap__ extends App {
    new ConsoleRunner().run(new __Bootstrap__())
}
