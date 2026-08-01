/**
 * @param {number[]} nums
 * @return {number}
 */
// 처음 푼방식 : 예외 [0,2,5,7] 일때 4로 나옴
// var longestArithSeqLength = function(nums) {
//     const map={};
//     let maxLen=1;

//     for(let i=0;i<nums.length;i++){
//         for(let j=0;j<i;j++){
//             const diff=nums[i]-nums[j];
//             if(map[diff]!==undefined) map[diff]++;
//             else map[diff]=2;
//             maxLen=Math.max(maxLen,map[diff]);
//         }
//     }
//     return maxLen;
// };
var longestArithSeqLength = function (nums) {
  // 인덱스별로 맵생성
  const map = Array.from({ length: nums.length }, () => ({}));
  let maxLen = 1;

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      const diff = nums[i] - nums[j];
      if (map[j][diff] !== undefined) map[i][diff] = map[j][diff] + 1;
      else map[i][diff] = 2;
      maxLen = Math.max(maxLen, map[i][diff]);
    }
  }
  return maxLen;
};
