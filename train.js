// G Task
function getHighestIndex(number) {
  const res = Math.max(...number);
  return number.indexOf(res);
}

console.log(getHighestIndex([2, 5, 1, 7]));

// //F Task
// function getHighestIndex(arr) {
//     const maxNumber = Math.max(...arr);
//     return arr.indexOf(maxNumber);
// }

// console.log(getHighestIndex([1, 4, 7, 13]));
