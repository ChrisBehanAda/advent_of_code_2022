// Package utils contains functions for common operations needed in advent of code.
package utils

func StringSlicesEqual(s1 []string, s2 []string) bool {
	if len(s1) != len(s2) {
		return false
	}
	for idx, val := range s1 {
		if s2[idx] != val {
			return false
		}
	}
	return true
}
