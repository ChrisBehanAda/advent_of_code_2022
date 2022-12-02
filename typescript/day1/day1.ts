import { readFile } from "../utils.ts";
function Part1(): number {
  const content = readFile("./day1/input.txt");
  const caloriesPerElf = totalCaloriesPerElf(content);
  const sortedCaloriesPerElf = caloriesPerElf.sort((a, b) => b - a);
  return sortedCaloriesPerElf[0];
}

function Part2(): number {
  const content = readFile("./day1/input.txt");
  const caloriesPerElf = totalCaloriesPerElf(content);
  const sortedCaloriesPerElf = caloriesPerElf.sort((a, b) => b - a);
  return sortedCaloriesPerElf[0] + sortedCaloriesPerElf[1] +
    sortedCaloriesPerElf[2];
}

function totalCaloriesPerElf(content: string): number[] {
  // convert input into one line of string per elf
  const rationsPerElfString = content.split("\n\n");
  // convert the line of string into a list of numbers representing calories
  const rationsPerElf = rationsPerElfString.map((line) => {
    const calorieStrings = line.split("\n");
    return calorieStrings.map((val) => Number(val));
  });
  const totalCaloriesPerElf = rationsPerElf.map((arr) => {
    return arr.reduce((acc, curr) => acc + curr);
  });
  return totalCaloriesPerElf;
}

console.log(Part1());

export { Part1, Part2 };
