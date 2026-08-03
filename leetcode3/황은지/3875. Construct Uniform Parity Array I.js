/**
 * @param {number[]} nums1
 * @return {boolean}
 */
var uniformArray = function (nums1) {
  //  모두 홀이나 짝이면 차이는 전부 짝 (홀-홀/ 짝-짝=짝)
  // 짝홀이 섞여있다면..?(짝-홀 / 홀-짝=홀)
  //짝홀이 섞여있다면.. 1,2,4,6 => 1,1,3,5 (2개이상이면 다가능) 하나면, 짝-홀 해서 홀조합으로..
  return true;
};
