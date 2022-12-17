package day9

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type move struct {
	direction string
	distance  int
}

type pos struct {
	x, y int
}

func (p pos) String() string {
	return fmt.Sprintf("%v,%v", p.x, p.y)
}

func getInput() []move {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)
	lines := strings.Split(input, "\n")
	moves := []move{}
	for _, l := range lines {
		dir := string(l[0])
		dist, err := strconv.Atoi(l[2:])
		if err != nil {
			panic(err)
		}
		m := move{direction: dir, distance: dist}
		moves = append(moves, m)
	}
	return moves
}

func Part1() int {
	moves := getInput()
	visited := map[string]int{}
	startPos := pos{x: 0, y: 0}
	handleMoves(visited, startPos, moves)
	ans := len(visited)
	return ans
}

func Part2() int {
	moves := getInput()
	visited := map[string]int{}
	startPos := pos{x: 0, y: 0}
	handleMoves2(visited, startPos, moves, 10)
	ans := len(visited)
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func handleMoves(visited map[string]int, startPos pos, moves []move) {
	head, tail := pos{x: startPos.x, y: startPos.y}, pos{x: startPos.x, y: startPos.y}
	visited[tail.String()] = 1
	for _, m := range moves {
		for i := 0; i < m.distance; i++ {
			makeMove(&head, m)
			if !adjacent(head, tail) {
				tail = getAlignedTail(head, tail)
			}
			visited[tail.String()] = 1
		}
	}
}

func handleMoves2(visited map[string]int, startPos pos, moves []move, ropeLength int) {
	rope := []pos{}
	for i := 0; i < ropeLength; i++ {
		p := pos{x: startPos.x, y: startPos.y}
		rope = append(rope, p)
	}
	for _, m := range moves {
		for i := 0; i < m.distance; i++ {
			makeMove(&rope[0], m)
			for j := 1; j < ropeLength; j++ {
				lead := rope[j-1]
				follow := rope[j]
				if !adjacent(lead, follow) {
					rope[j] = getAlignedTail(lead, follow)
				}
				// Mark where the tail visited
				if j == len(rope)-1 {
					visited[rope[j].String()] = 1
				}
			}
		}
	}
}

func makeMove(p *pos, m move) {
	switch m.direction {
	case "R":
		p.x++
	case "L":
		p.x--
	case "U":
		p.y++
	case "D":
		p.y--
	}
}

// 2 points are adjacent if both their x and y coordinates are between 0-1
// positions apart.
func adjacent(head, tail pos) bool {
	xDiff := abs(head.x - tail.x)
	yDiff := abs(head.y - tail.y)
	if xDiff <= 1 && yDiff <= 1 {
		return true
	}
	return false
}

func getAlignedTail(head, tail pos) pos {
	xDir := getDiffSign(head.x, tail.x)
	yDir := getDiffSign(head.y, tail.y)
	newTail := pos{x: tail.x + xDir, y: tail.y + yDir}
	return newTail
}

// Returns 1 if a is greater than b, -1 if a is smaller than b
// and 0 if a and b are the same.
func getDiffSign(a, b int) int {
	if a > b {
		return 1
	} else if a < b {
		return -1
	} else {
		return 0
	}
}
