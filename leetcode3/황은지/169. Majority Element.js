/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const map = new Map();

  for (const num of nums) {
    const count = (map.get(num) || 0) + 1;
    map.set(num, count);

    if (count >= nums.length / 2) return num;
  }
};
