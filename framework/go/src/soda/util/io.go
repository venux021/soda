package util

import "fmt"
import "os"

type SimpleLogger struct {}

var Logger SimpleLogger = SimpleLogger{}

func (g *SimpleLogger) Finfo(format string, a ...interface{}) {
    fmt.Fprintf(os.Stderr, "[INFO] " + format + "\n", a...)
}

func (g *SimpleLogger) Ferror(format string, a ...interface{}) {
    fmt.Fprintf(os.Stderr, "[ERROR] " + format + "\n", a...)
}

func PrintErr(format string, a ...interface{}) (n int, err error) {
    return fmt.Fprintf(os.Stderr, format, a...)
}
