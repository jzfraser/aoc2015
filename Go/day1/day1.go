package main

import (
    "fmt"

    "util"
)

func main() {
    input := util.GetInput("day1input.txt")
    // inputString := "(((("
    // input := []rune(inputString)
    floor := 0
    firstTime := true
    var wentNegative int
    for i := 0; i < len(input); i++ {
        // fmt.Println(string(input[i]))
        char := string(input[i])
        if char == "(" {
            floor += 1
        } else if char == ")" {
            floor -= 1
        }

        if floor < 0 && firstTime {
            wentNegative = i + 1
            firstTime = false
        }
    }
    fmt.Printf("Day1 part 1: floor %d\n", floor)
    if firstTime {
        fmt.Println("Day 1 part 2: never went to a negative floor")
    } else {
        fmt.Printf("Day1 part 2: went negative for first time on %d\n", wentNegative)
    }
}
