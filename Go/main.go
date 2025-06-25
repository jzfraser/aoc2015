package main

import (
	"fmt"
	"strings"
)

var days = map[string]func(){
	"1": day1,
	"2": day2,
}

func main() {
	for true {
		var day string
		var input string

		fmt.Print("Enter the day number (1-25) or Q to quit: ")
		fmt.Scanln(&input)

		input = strings.TrimSpace(input)
		day = strings.ToLower(input)

		if day == "q" {
			fmt.Println("Exiting the program.")
			return
		}

		if fn, ok := days[day]; ok {
			clearScreen()
			fn()
		} else {
			fmt.Println("Invalid day number. Please enter a number between 1 and 25 or Q to quit.")
		}
	}
}
