// 1 2 3 4    --->    2 1 4 3
function replaceWithNext(array) {
  if (array.length % 2) {
    console.log("bruh this will not work");
    console.log("make sure the length of the array is even");
    return;
  }
  let oddIndex = [];
  let noOfOddIndex = 0;
  let evenIndex = [];
  let noOfEvenIndex = 0;
  let result = [];
  for (let i = 0; i < array.length; i++) {
    if (i % 2) {
      oddIndex.push(array[i]);
    } else {
      evenIndex.push(array[i]);
    }
  }
  for (let i = 0; i < array.length; i++) {
    if (i % 2) {
      result.push(evenIndex[noOfEvenIndex]);
      noOfEvenIndex++;
    } else {
      result.push(oddIndex[noOfOddIndex]);
      noOfOddIndex++;
    }
  }
  return result;
}

console.log(replaceWithNext([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]));
