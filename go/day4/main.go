package day4

import (
	"os"
	"strconv"
	"strings"
)

func main() {

}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getLines(path string) []string {
	data, err := os.ReadFile(path)
	check(err)
	content := string(data)
	return strings.Split(content, "\n")
}

func Part1() int {
	return countSectionEvents(fullOverlap)
}

func Part2() int {
	return countSectionEvents(anyOverlap)
}

func countSectionEvents(countEvent func(int, int, int, int) bool) int {
	lines := getLines("input.txt")
	count := 0
	for _, l := range lines {
		sections := strings.Split(l, ",")
		section1, section2 := sections[0], sections[1]
		section1Ranges := strings.Split(section1, "-")
		section2Ranges := strings.Split(section2, "-")
		section1Start, err := strconv.Atoi(section1Ranges[0])
		check(err)
		section1End, err := strconv.Atoi(section1Ranges[1])
		check(err)
		section2Start, err := strconv.Atoi(section2Ranges[0])
		check(err)
		section2End, err := strconv.Atoi(section2Ranges[1])
		check(err)
		if countEvent(section1Start, section1End, section2Start, section2End) {
			count++
		}
	}
	return count
}

func anyOverlap(start1 int, end1 int, start2 int, end2 int) bool {
	if start1 <= end2 && end1 >= start2 {
		return true
	}
	return false
}

func fullOverlap(start1 int, end1 int, start2 int, end2 int) bool {
	// interval 1 within interval 2
	if start1 >= start2 && end1 <= end2 {
		return true
	}
	// interval 2 within interval 1
	if start2 >= start1 && end2 <= end1 {
		return true
	}
	return false
}
