package day8

import (
	"os"
	"strconv"
	"strings"
)

func getInput() [][]int {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)
	lines := strings.Split(input, "\n")
	grid := [][]int{}
	for _, l := range lines {
		row := []int{}
		for _, r := range l {
			char := string(r)
			charAsInt, _ := strconv.Atoi(char)
			row = append(row, charAsInt)
		}
		grid = append(grid, row)
	}
	return grid
}

func get2dBoolGrid(rows, cols int) [][]bool {
	visited := [][]bool{}
	for row := 0; row < rows; row++ {
		r := []bool{}
		for col := 0; col < cols; col++ {
			r = append(r, false)
		}
		visited = append(visited, r)
	}
	return visited
}

func Part1() int {
	grid := getInput()
	count := 0
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			if seenFromEdge(grid, r, c) {
				count++
			}
		}
	}
	return count
}

func Part2() int {
	grid := getInput()
	max := -1
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			score := scenicScore(grid, r, c)
			if score > max {
				max = score
			}
		}
	}
	return max
}

func seenFromEdge(grid [][]int, row, col int) bool {
	// Return true if coordinate is on the edge of the grid
	if row == 0 || row == len(grid)-1 || col == 0 || col == len(grid[0])-1 {
		return true
	}
	// Check if tree can be seen from the top of the grid
	seenFromTop := true
	for r := row - 1; r >= 0; r-- {
		if grid[r][col] >= grid[row][col] {
			// Once we encounter a tree north of the origin tree that is taller
			// break out of the loop.
			seenFromTop = false
			break
		}
	}
	if seenFromTop {
		return true
	}

	seenFromBottom := true
	for r := row + 1; r < len(grid); r++ {
		if grid[r][col] >= grid[row][col] {
			// Once we encounter a tree south of the origin tree that is taller
			// break out of the loop.
			seenFromBottom = false
			break
		}
	}
	if seenFromBottom {
		return true
	}

	seenFromLeft := true
	for c := col - 1; c >= 0; c-- {
		if grid[row][c] >= grid[row][col] {
			seenFromLeft = false
			break
		}
	}
	if seenFromLeft {
		return true
	}

	seenFromRight := true
	for c := col + 1; c < len(grid[0]); c++ {
		if grid[row][c] >= grid[row][col] {
			seenFromRight = false
			break
		}
	}
	if seenFromRight {
		return true
	}

	return false
}

func scenicScore(grid [][]int, row, col int) int {
	upScore := 0
	if row > 0 {
		for r := row - 1; r >= 0; r-- {
			upScore++
			if grid[r][col] >= grid[row][col] {
				break
			}
		}
	}

	downScore := 0
	if row < len(grid)-1 {
		for r := row + 1; r < len(grid); r++ {
			downScore++
			if grid[r][col] >= grid[row][col] {
				break
			}
		}
	}

	leftScore := 0
	if col > 0 {
		for c := col - 1; c >= 0; c-- {
			leftScore++
			if grid[row][c] >= grid[row][col] {
				break
			}
		}
	}

	rightScore := 0
	if col < len(grid)-1 {
		for c := col + 1; c < len(grid[0]); c++ {
			rightScore++
			if grid[row][c] >= grid[row][col] {
				break
			}
		}
	}

	return upScore * downScore * leftScore * rightScore
}

// Perform a dfs from the starting coordinate to one of the edges if possible.
// Return true if you can reach the end, false otherwise.
func dfsToEdge(grid [][]int, row, col int, visited [][]bool, original int) bool {
	// Return true if coordinate is on the edge of the grid
	if row == 0 || row == len(grid)-1 || col == 0 || col == len(grid[0])-1 {
		return true
	}
	if visited[row][col] {
		return false
	}

	visited[row][col] = true

	if row > 0 && grid[row-1][col] < original {
		reachGoingUp := dfsToEdge(grid, row-1, col, visited, original)
		if reachGoingUp {
			return true
		}
	}

	if row < len(grid)-1 && grid[row+1][col] < original {
		reachGoingDown := dfsToEdge(grid, row+1, col, visited, original)
		if reachGoingDown {
			return true
		}
	}

	if col > 0 && grid[row][col-1] < original {
		reachGoingLeft := dfsToEdge(grid, row, col-1, visited, original)
		if reachGoingLeft {
			return true
		}
	}
	if col < len(grid[0])-1 && grid[row][col+1] < original {
		reachGoingRight := dfsToEdge(grid, row, col+1, visited, original)
		if reachGoingRight {
			return true
		}
	}
	return false
}
