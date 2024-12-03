package main 

import "fmt"
import "bufio"
import "os"


func read_file() {
  fname = "example_data.txt"
  file, err = os.Open(fname) 
  if err != nil:
    fmt.Println("Error opening file")
}

func main() {
  read_file()
}
