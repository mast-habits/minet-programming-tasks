function stringReverse(string) {
  let result = [];
  for (let i = string.length; i >= 0; i--) {
    result.push(string[i - 1]);
  }
  return result.join("");
}

// for words
function wordPalindromeChecker(word) {
  word = word.toLowerCase();
  let toCheck;
  if (word.length % 2) {
    toCheck = word.length / 2 - 0.5;
  } else {
    toCheck = word.length / 2;
  }
  if (word.slice(0, toCheck) == stringReverse(word.slice(-toCheck))) {
    return true;
  } else {
    return false;
  }
}

// for sentences
function sentencePalindromeChecker(sentence) {
  return wordPalindromeChecker(sentence.replace(/ /g, ""));
}

console.log(sentencePalindromeChecker("too hot to hoot"));
