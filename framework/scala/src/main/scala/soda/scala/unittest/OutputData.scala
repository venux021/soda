package soda.scala.unittest

class OutputData {

    var id: Int = 0

    var success: Boolean = false

    var result: Object = null

    var elapse: Double = 0.0

    def setResult(res: Object): Unit = result = res

    def getResult[T](klass: Class[T]): T = klass.cast(result)

}
