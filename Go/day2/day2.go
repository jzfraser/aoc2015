package main

import (
    "fmt"
    "slices"
    "strconv"
    "strings"

    "util"
)

func main() {
    input := util.GetInput("day2input.txt")
    inputs := strings.Split(string(input), "\n")
    wrappingPaper := 0
    ribbon := 0
    for _, i := range inputs {
        dims := strings.Split(i, "x")
        // fmt.Println(dims)

        l, lErr := strconv.Atoi(dims[0])
        w, wErr := strconv.Atoi(dims[1])
        h, hErr := strconv.Atoi(dims[2])
        if lErr != nil || wErr != nil || hErr != nil {
            panic("failed to get dimension")
        }

        lwh := []int{l, w, h}
        slices.Sort(lwh)
        low1 := lwh[0]
        low2 := lwh[1]

        // fmt.Printf("dims %dx%dx%d with low1 %d, low2 %d\n", l, w, h, low1, low2)

        wrappingPaper += 2 * (l * w + w * h + h * l) + (low1 * low2)
        ribbon += (l * w * h) + (2 * low1 + 2 * low2)
    }
    fmt.Printf("Day 2 part 1: wrapping paper required is %d feet\n", wrappingPaper)
    fmt.Printf("Day 2 part 2: ribbon required is %d feet\n", ribbon)
}
