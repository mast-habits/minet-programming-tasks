function replaceSpace(string, key) {
  return string.replace(/ /g, key);
}

console.log(replaceSpace("Hello world", "#"));
