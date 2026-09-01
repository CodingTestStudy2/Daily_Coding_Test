/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndices = function (nums) {
  const len = nums.length;

  let count = 0;
  let sum = nums[len - 1];

  for (let i = len - 2; i >= 0; i--) {
    if (nums[i] > sum / (len - i - 1)) count++;
    sum += nums[i];
  }

  return count;
};
