# Test problem in preparation for advent of code 2022

def fizz_buzz(n: int):
    ans = []
    for i in range(1, n + 1):
        val = ""
        if i % 3 == 0:
            val += "Fizz"
        if i % 5 == 0:
            val += "Buzz"
        if not val:
            val = str(i)
        ans.append(val)
    return ans
        