package day7

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	expected := 1141028
	ans := Part1()
	if ans != expected {
		t.Errorf("Expected %v, got %v", expected, ans)
	}
}

func TestPart2(t *testing.T) {
	expected := 8278005
	ans := Part2()
	if ans != expected {
		t.Errorf("Expected %v, got %v", expected, ans)
	}
	Part2()
}

func TestIsCDLine(t *testing.T) {
	dirName := "testdir123"
	input := fmt.Sprintf("$ cd %v", dirName)
	isCDLine(input)
	isCD, dir := isCDLine(input)
	if !isCD || dir != dirName {
		t.Error("Invalid response")
	}
}
func TestIsLSLine(t *testing.T) {
	isLS := isLSLine("$ ls")
	if !isLS {
		t.Error("Unexpected value")
	}
}

func TestIsDIRLine(t *testing.T) {
	isDir, dir := isDirLine("dir test123")
	if !isDir || dir != "test123" {
		t.Error("Unexpected value")
	}
}

func TestIsFileLine(t *testing.T) {
	isFile, fileSize, fileName := isFileLine("8504156 c.dat")
	if !isFile || fileSize != 8504156 || fileName != "c.dat" {
		t.Error("Unexpected value")
	}
}
