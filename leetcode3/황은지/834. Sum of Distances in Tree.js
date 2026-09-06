/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var sumOfDistancesInTree = function (n, edges) {
  const dp = Array.from({ length: 6 }, () => Array(6));
  // 미리 2차원 배열에 채운다
  // root에서 내려가면서 한번만 계산하는 방법이 없을까?
  // dfs n번 돌리니 시간초과됨.. dp를 써야될거같은데 방법을 못찾음..
};
