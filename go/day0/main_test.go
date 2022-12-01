package day0

import (
	"advent_of_code_2022/utils"
	"testing"
)

func TestFizzBuzz(t *testing.T) {
	n := 15
	expected := []string{"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"}

	result := FizzBuzz(n)

	if !utils.StringSlicesEqual(result, expected) {
		t.Errorf("Result was %v, expected %v", result, expected)
	}
}
