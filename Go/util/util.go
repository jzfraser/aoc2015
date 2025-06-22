package util

import (
	// "fmt"
	"os"
	"strings"
)

func GetInput(filepath string) []rune {
	prefix := "../../inputs/"
	dat, err := os.ReadFile(prefix + filepath)
	if err != nil {
		panic(err)
	}

	inputString := string(dat[:])
	inputString = strings.TrimSpace(inputString)
	inputRunes := []rune(inputString)
	// fmt.Println(string(inputRunes))
	return inputRunes
}
