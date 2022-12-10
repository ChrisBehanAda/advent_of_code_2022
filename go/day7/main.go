package day7

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {

}

type file struct {
	name string
	size int
}

type directory struct {
	name   string
	dirs   []*directory
	files  []file
	parent *directory
}

func isCDLine(line string) (bool, string) {
	cdRegex := `\$ cd (.+)`
	pattern, err := regexp.Compile(cdRegex)
	if err != nil {
		panic(err)
	}
	match := pattern.FindStringSubmatch(line)
	if len(match) > 0 {
		fmt.Print(match[1])
		return true, match[1]
	}
	return false, ""
}

func isLSLine(line string) bool {
	cdRegex := `\$ ls`
	pattern, err := regexp.Compile(cdRegex)
	if err != nil {
		panic(err)
	}
	match := pattern.Match([]byte(line))
	if match {
		return true
	}
	return false
}

func isDirLine(line string) (bool, string) {
	dirRegex := `dir (.+)`
	pattern, err := regexp.Compile(dirRegex)
	if err != nil {
		panic(err)
	}
	match := pattern.FindStringSubmatch(line)
	if len(match) > 0 {
		fmt.Print(match[1])
		return true, match[1]
	}
	return false, ""
}

func isFileLine(line string) (bool, int, string) {
	fileRegex := `([0-9]+) (.+)`
	pattern, err := regexp.Compile(fileRegex)
	if err != nil {
		panic(err)
	}
	match := pattern.FindStringSubmatch(line)
	if len(match) > 0 {
		fileSize, _ := strconv.Atoi(match[1])
		fileName := match[2]
		return true, fileSize, fileName
	}
	return false, 0, ""
}

const (
	cdLine   = iota
	lsLine   = iota
	dirLine  = iota
	fileLine = iota
)

func getLineType(line string) int {
	if string(line[0]) == "$" {
		command := line[2:4]
		if command == "cd" {
			return cdLine
		} else if command == "ls" {
			return lsLine
		} else {
			err := fmt.Errorf("Unexpected command: %v", command)
			panic(err)
		}
	} else if line[0:3] == "dir" {
		return dirLine
	} else if _, err := strconv.Atoi(string(line[0])); err == nil {
		return fileLine
	} else {
		err := fmt.Errorf("Unexpected line: %v", line)
		panic(err)
	}
}

func Part1() int {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)
	lines := strings.Split(input, "\n")
	fs := buildFileStructure(lines)
	sizes := directorySizes(*fs, []string{}, map[string]int{})

	ans := 0
	for _, size := range sizes {
		if size <= 100000 {
			ans += size
		}
	}

	return ans
}

func Part2() int {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(data)
	lines := strings.Split(input, "\n")
	fs := buildFileStructure(lines)
	sizes := directorySizes(*fs, []string{}, map[string]int{})
	inUseSpace := sizes["/"]
	availableSpace := 70000000
	requiredSpace := 30000000
	freeSpace := availableSpace - inUseSpace
	min := 99999999999
	for _, size := range sizes {
		if freeSpace+size >= requiredSpace {
			if size < min {
				min = size
			}
		}
	}
	return min
}

func directorySizes(dir directory, parentsNames []string, sizes map[string]int) map[string]int {
	for _, f := range dir.files {
		if _, found := sizes[dir.name]; !found {
			sizes[dir.name] = f.size
		} else {
			sizes[dir.name] += f.size
		}
		for _, n := range parentsNames {
			sizes[n] += f.size
		}
	}
	parentsNames = append(parentsNames, dir.name)

	for _, d := range dir.dirs {
		directorySizes(*d, parentsNames, sizes)
	}
	return sizes
}

func findDirByName(dirs []*directory, name string) *directory {
	for _, d := range dirs {
		if d.name == name {
			return d
		}
	}
	return nil
}

func getPathName(parent string, current string) string {
	path := "/" + current
	if parent != "/" {
		path = parent + path
	}
	return path
}

func buildFileStructure(lines []string) *directory {
	root := &directory{name: "/"}
	res := root
	for _, l := range lines[1:] {
		if isLSLine(l) {

		} else if isDir, dirName := isDirLine(l); isDir {
			pathName := getPathName(root.name, dirName)
			childDir := &directory{name: pathName, parent: root}
			if root.dirs == nil {
				root.dirs = []*directory{childDir}
			} else {
				root.dirs = append(root.dirs, childDir)
			}
		} else if isFile, fileSize, fileName := isFileLine(l); isFile {
			f := file{name: fileName, size: fileSize}
			root.files = append(root.files, f)
		} else if isCd, dirName := isCDLine(l); isCd {
			if dirName == ".." {
				root = root.parent
			} else if dirName == "/" {
				root = res
			} else {
				pathName := getPathName(root.name, dirName)
				root = findDirByName(root.dirs, pathName)
			}
		}
	}
	return res
}
