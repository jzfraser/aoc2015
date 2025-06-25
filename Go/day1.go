package main

import (
	"fmt"
)

func day1() {
	input := GetInput("day1input.txt")
	// inputString := "(((("
	// input := []rune(inputString)
	floor := 0
	firstTime := true
	var wentNegative int
	for i := range input {
		// fmt.Println(string(input[i]))
		char := string(input[i])
		switch char {
		case "(":
			floor += 1
		case ")":
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
