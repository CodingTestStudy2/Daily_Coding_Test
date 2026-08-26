/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var limitOccurrences = function (nums, k) {
  const count = Array(101).fill(0);
  const result = [];

  const putNumber = function (num, repeat) {
    for (let i = 0; i < repeat; i++) {
      result.push(num);
    }
  };

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    count[num]++;
    if (i === nums.length - 1 || num !== nums[i + 1]) {
      if (count[num] <= k) putNumber(num, count[num]);
      else putNumber(num, k);
    }
  }

  return result;
};
