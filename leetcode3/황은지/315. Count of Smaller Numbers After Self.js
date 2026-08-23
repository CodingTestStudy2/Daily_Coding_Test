/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function (nums) {
  const output = Array(nums.length);
  // 이렇게 하니까 잘못 참조 함..
  for (let i = nums.length - 1; i >= 0; i--) {
    output[i] = 0;
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] <= nums[i]) {
        if (nums[j] === nums[i]) output[i] = output[j];
        else output[i] = output[j] + 1;
        break;
      }
    }
  }

  return output;
};
