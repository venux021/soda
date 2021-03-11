package util

import "fmt"
import "os"

func PrintErr(format string, a ...interface{}) (n int, err error) {
    return fmt.Fprintf(os.Stderr, format, a...)
}
