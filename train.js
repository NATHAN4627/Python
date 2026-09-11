//G Task
function getHighestIndex(arr) {
    const maxNumber = Math.max(...arr);
    return arr.indexOf(maxNumber);
}

console.log(getHighestIndex([1, 4, 7, 13]));
