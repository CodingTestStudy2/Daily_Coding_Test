/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestInteger = function (nums, k) {
  if (nums.length < k) return -1;
  if (nums.length === k) return Math.max(...nums);

  const group = {};
  let max = -1;
  // k가 1이면 중간에 겹치는거 없으면 됨
  // 양쪽 끝은 중간에 숫자가 없으면 안겹침

  for (let i = 0; i < nums.length; i++) {
    if (k !== 1 && (i == 0 || i == nums.length - 1)) continue;
    group[nums[i]] = (group[nums[i]] || 0) + 1;
  }

  if (k !== 1) {
    const left = nums[0];
    const right = nums[nums.length - 1];
    if (left === right) return -1;
    if (group[left] === undefined) max = Math.max(max, left);
    if (group[right] === undefined) max = Math.max(max, right);
  } else {
    for (const [key, value] of Object.entries(group)) {
      if (value === 1) max = Math.max(key);
    }
  }
  return max;
};
