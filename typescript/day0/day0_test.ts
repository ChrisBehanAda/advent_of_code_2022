import { assertEquals } from "https://deno.land/std@0.166.0/testing/asserts.ts";
import { FizzBuzz } from "./day0.ts";

Deno.test("FizzBuzz test", () => {
  const n = 15;
  const expected = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
  ];
  const result = FizzBuzz(n);
  assertEquals(result, expected);
});
