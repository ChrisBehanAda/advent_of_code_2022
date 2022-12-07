package day6

import (
	"fmt"
	"os"
)

func main() {
	fmt.Print("Hello")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func Part1() int {
	data, err := os.ReadFile("input.txt")
	check(err)
	dataStream := string(data)
	return positionOfUniqueChars(4, dataStream)
}

func Part2() int {
	data, err := os.ReadFile("input.txt")
	check(err)
	dataStream := string(data)
	return positionOfUniqueChars(14, dataStream)
}

func positionOfUniqueChars(uniqueCount int, input string) int {
	chars := map[rune]bool{}
	p1 := 0
	p2 := 0
	for p2 < len(input) {
		cur := rune(input[p2])
		if !chars[cur] {
			chars[cur] = true
			p2++
		} else {
			chars = map[rune]bool{}
			p1++
			p2 = p1
		}

		if p2-p1 == uniqueCount {
			return p2
		}
	}
	return -1
}
