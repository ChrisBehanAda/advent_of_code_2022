package day1

import "testing"

func TestPart1(t *testing.T) {
	ans := 69281
	res := Part1()
	if ans != res {
		t.Errorf("unexpected answer")
	}
}

func TestPart2(t *testing.T) {
	ans := 201524
	res := Part2()
	if ans != res {
		t.Errorf("unexpected answer")
	}
}
