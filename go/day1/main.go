package day1

import (
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

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
	lines := getLines("input.txt")
	elvesTotalCalories := totalCaloriesPerElf(lines)
	return max(elvesTotalCalories)
}

func Part2() int {
	lines := getLines("input.txt")
	elvesTotalCalories := totalCaloriesPerElf(lines)
	sort.Ints(elvesTotalCalories)
	return elvesTotalCalories[len(elvesTotalCalories)-1] + elvesTotalCalories[len(elvesTotalCalories)-2] + elvesTotalCalories[len(elvesTotalCalories)-3]
}

func totalCaloriesPerElf(lines []string) []int {
	elfRations := [][]int{}
	currentElfsRations := []int{}
	for _, l := range lines {
		if l == "" {
			elfRations = append(elfRations, currentElfsRations)
			currentElfsRations = []int{}
		} else {
			trimmedLine := strings.Trim(l, "\n")
			calories, err := strconv.Atoi(trimmedLine)
			check(err)
			currentElfsRations = append(currentElfsRations, calories)
		}
	}
	elvesTotalCalories := []int{}
	for _, rationsSlice := range elfRations {
		calorieSum := sum(rationsSlice)
		elvesTotalCalories = append(elvesTotalCalories, calorieSum)
	}

	return elvesTotalCalories
}

func sum(nums []int) int {
	s := 0
	for _, n := range nums {
		s += n
	}
	return s
}

func max(nums []int) int {
	m := math.MinInt
	for _, n := range nums {
		if n > m {
			m = n
		}
	}
	return m
}
