package main 

import "fmt"
import "bufio"
import "os"
func read_file() {
    fname := "example_data.txt" // Declare the variable fname with ":="
    file, err := os.Open(fname)  // Declare file and err with ":=" for assignment
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }
    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
    }
}

func main() {
    read_file()
}
