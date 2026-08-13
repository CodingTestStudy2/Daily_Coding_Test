/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function (nums) {
  // 가장 긴 변이 나머지 두변 합보다 작아야됨
  let count = 0;
  nums.sort((a, b) => b - a);

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] >= nums[j] + nums[k]) break;
        count++;
      }
    }
  }

  return count;
};
