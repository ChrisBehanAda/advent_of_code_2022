package day9

import (
	"testing"
)

func TestPart1(t *testing.T) {
	expected := 5619
	ans := Part1()
	if ans != expected {
		t.Errorf("Expected %v, got %v", expected, ans)
	}
}

func TestPart2(t *testing.T) {
	expected := 2376
	ans := Part2()
	if ans != expected {
		t.Errorf("Expected %v, got %v", expected, ans)
	}
}
