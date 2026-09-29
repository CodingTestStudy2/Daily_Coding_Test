/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function (nums) {
  if (nums.length < 3) return 0;
  const diff = Array(nums.length - 1);
  let count = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    diff[i] = nums[i + 1] - nums[i];
  }

  let prevDiff = diff[0];
  let startIndex = 0;
  for (let i = 1; i < diff.length; i++) {
    if (diff[i] !== prevDiff) {
      if (i - 1 !== startIndex) {
        const sameCount = i - startIndex;
        let plus = sameCount - 2 + 1;
        while (plus > 0) {
          count += plus--;
        }
      }
      startIndex = i;
      prevDiff = diff[i];
    }
  }

  if (startIndex !== diff.length - 1) {
    const sameCount = diff.length - startIndex;
    let plus = sameCount - 2 + 1;
    while (plus > 0) {
      count += plus--;
    }
  }

  return count;
};
