function readFile(path: string): string {
  return Deno.readTextFileSync(path);
}

function readLinesInFile(path: string): string[] {
  const content = readFile(path);
  return content.split("\n");
}

export { readFile, readLinesInFile };
