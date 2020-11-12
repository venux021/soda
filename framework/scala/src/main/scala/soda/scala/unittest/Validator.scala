package soda.scala.unittest

trait Validator[T] {
    def validate(expect: T, result: T): Boolean
}
