// K Task

function countVowels(str) {
  const vowels = ["a", "e", "o", "i", "u"];
  res = str.toLowerCase();
  count = 0;
  for (let i = 0; i < str.length; i++) {
    if (vowels.includes(res[i])) {
      count++;
    }
  }
  return count;
}

console.log(countVowels("Engineering"));

// Shunday function yozing,
// u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
// MASALAN: countVowels("string") return 1.

// F Task

// function findDoublers(str) {
//   for (let i = 0; i < str.length; i++) {
//     for (let j = i + 1; j < str.length; j++) {
//       if (str[i] === str[j]) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

// console.log(findDoublers("nathan"));

//G Task
// function getHighestIndex(arr) {
//     const maxNumber = Math.max(...arr);
//     return arr.indexOf(maxNumber);
// }

// console.log(getHighestIndex([1, 4, 7, 13]));
