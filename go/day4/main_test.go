package day4

import "testing"

func TestPart1(t *testing.T) {
	ans := Part1()
	if ans != 518 {
		t.Errorf("Expected %v, but got %v", 518, ans)
	}
}

func TestPart2(t *testing.T) {
	ans := Part2()
	if ans != 909 {
		t.Errorf("Expected %v, but got %v", 909, ans)
	}
}
