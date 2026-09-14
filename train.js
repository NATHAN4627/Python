// F Task

function findDoublers(str) {
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length; j++) {
      if (str[i] === str[j]) {
        return true;
      }
    }
  }
  return false;
}

console.log(findDoublers("nathan"));

//G Task
// function getHighestIndex(arr) {
//     const maxNumber = Math.max(...arr);
//     return arr.indexOf(maxNumber);
// }

// console.log(getHighestIndex([1, 4, 7, 13]));
