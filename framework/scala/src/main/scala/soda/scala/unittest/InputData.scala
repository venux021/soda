package soda.scala.unittest

import java.util.{List => JList}

class InputData {

    var id: Int = 0

    var expected: Object = null

    var args: JList[Object] = null

    def arg(index: Int): Object = {
        if (args == null && args.size() > index)
            args.get(index)
        else
            null
    }

    def hasExpected(): Boolean = expected != null

    def getExpected[T](klass: Class[T]): T = klass.cast(expected)

}
