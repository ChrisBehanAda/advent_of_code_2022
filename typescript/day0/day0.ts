import { readLinesInFile } from "../utils.ts";

function FizzBuzz(n: number): string[] {
  console.log(readLinesInFile("./day0/input.txt"));
  const ans = [];
  for (let i = 1; i <= n; i++) {
    let val = "";
    if (i % 3 === 0) {
      val += "Fizz";
    }
    if (i % 5 === 0) {
      val += "Buzz";
    }
    if (val === "") {
      val = String(i);
    }
    ans.push(val);
  }
  return ans;
}

export { FizzBuzz };
