package day0

import "strconv"

func FizzBuzz(n int) []string {
	ans := []string{}
	for i := 1; i <= n; i++ {
		val := ""
		if i%3 == 0 {
			val += "Fizz"
		}
		if i%5 == 0 {
			val += "Buzz"
		}
		if val == "" {
			val = strconv.Itoa(i)
		}
		ans = append(ans, val)
	}
	return ans
}
