/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let start = 0;
  let count = 0;
  let maxLen = 0;

  for (let end = 0; end < nums.length; end++) {
    if (nums[end] === 0) count++;

    while (count > k) {
      if (nums[start++] === 0) count--;
    }
    maxLen = Math.max(maxLen, end - start + 1);
  }
  return maxLen;
};
