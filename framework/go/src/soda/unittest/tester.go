package unittest

import (
    "bufio"
    "os"
)

func ReadStdin() string {
    scanner := bufio.NewScanner(os.Stdin)
    content := ""
    for scanner.Scan() {
        line := scanner.Text()
        content += line
    }
    return content
}

