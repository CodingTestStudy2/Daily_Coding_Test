/**
 * @param {number[]} nums
 * @return {number}
 */
// 유클리드 호제법
var maxPairStrength = function (nums) {
  function findGCD(x, y) {
    while (y) {
      const temp = y;
      y = x % y;
      x = temp;
    }
    return x;
  }

  let maximum = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const gcd = findGCD(nums[i], nums[j]);
      maximum = Math.max((nums[i] / gcd) * (nums[j] / gcd), maximum);
    }
  }

  return maximum;
};

//  // 미통과
// var maxPairStrength = function(nums) {
//     // gcd = 최대공약수
//     // (ax * ay)/a^2 = x*y
//     // 즉 양쪽 모두에 포함되지않는 소수를 모두 곱하면 된다
//     // 소수를 다체크해야될까?? 그리고 쌍도 모든쌍을 다비교해봐야될까?
//     // 다 비교하니 시간초과..(2000*2000*10^5)

//     let maximum=0;

//     for(let i=0;i<nums.length;i++){
//         for(let j=i+1;j<nums.length;j++){
//             // x*y 계산하기
//             // 최대공약수 제거하기
//             const minNum=Math.min(nums[i],nums[j]);
//             for(let num=minNum;num>0;num--){
//                 if(nums[i]%num===0 && nums[j]%num===0){
//                     // 둘다 나눠지면 최대공약수에 해당
//                     maximum=Math.max(maximum,(nums[i]/num)*(nums[j]/num))
//                     break;
//                 }
//             }
//         }
//     }
//     return maximum;

// };
