package day6

import (
	"testing"
)

func TestPart1(t *testing.T) {
	ans := Part1()
	if ans != 1816 {
		t.Fatalf("Expected %v, got %v", 1816, ans)
	}
}

func TestPart2(t *testing.T) {
	ans := Part2()
	if ans != 2625 {
		t.Fatalf("Expected %v, got %v", 2625, ans)
	}
}
