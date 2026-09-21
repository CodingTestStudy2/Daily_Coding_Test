/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits; // 1을 더했으므로 즉시 배열 반환
    }

    digits[i] = 0;
  }

  digits.unshift(1);
  return digits;
};
