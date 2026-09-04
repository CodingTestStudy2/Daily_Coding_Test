/**
 * @param {number[]} nums
 * @return {number}
 */
var maxDigitRange = function (nums) {
  let maxDigitRange = 0;
  let maxSet = [];

  for (const num of nums) {
    const str = String(num);
    let largest = "0";
    let smallest = "9";
    for (const digit of str) {
      largest = Math.max(digit, largest);
      smallest = Math.min(digit, smallest);
    }
    const digitRange = largest - smallest;
    if (digitRange > maxDigitRange) {
      maxDigitRange = digitRange;
      maxSet = [num];
    } else if (digitRange === maxDigitRange) {
      maxSet.push(num);
    }
  }

  return maxSet.reduce((cur, acc) => cur + acc, 0);
};
