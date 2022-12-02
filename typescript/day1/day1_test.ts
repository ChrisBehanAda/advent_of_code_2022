import { assertEquals } from "https://deno.land/std@0.166.0/testing/asserts.ts";

import { Part1, Part2 } from "./day1.ts";

Deno.test("Part 1 test", () => {
  const expected = 69281;
  const answer = Part1();
  assertEquals(answer, expected);
});

Deno.test("Part 2 test", () => {
  const expected = 201524;
  const answer = Part2();
  assertEquals(answer, expected);
});
