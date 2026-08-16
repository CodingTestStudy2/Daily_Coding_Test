/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function (nums) {
  // 모든 순열 조합으로 하면 너무 숫자가 커짐(300!)..
  // 단순히 생각햇을땐, 가장 작은수부터 빨리 터뜨려야 이후 연쇄 곱셉에 큰수가 같이 곱해짐
  let coins = 0;
  nums.sort((a, b) => a - b);
  const arrNum = [...nums];
  let p = 0;

  while (arrNum.length > 0) {
    const minNum = nums[p++];
    for (let i = 0; i < arrNum.length; i++) {
      if (arrNum[i] === minNum) {
        const leftNum = i === 0 ? 1 : arrNum[i - 1];
        const rightNum = i === arrNum.length - 1 ? 1 : arrNum[i + 1];
        arrNum.splice(i, 1);
        break;
      }
    }
  }
  return coins;
};
