/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function (n, k, maxPts) {
  // 숫자는 최대 maxPts 까지 랜덤으로 나옴
  // k와 같거나 더 높은 숫자가 나오면 stop
  // n보다 작거나 같은 포인트가 나올확률을 구해라
  // 각각은 독립시행

  // Ex3의 경우에 받을수있는 포인트의 종류(하지만 확률은 다 다름)
  // 17, 18, 19, 20, 21, 22, 23, 24, 25, 26

  const dp = Array(k + maxPts);
  dp[0] = 0;
  for (let i = 1; i < dp.length; i++) {
    for (let j = 0; j < i; j++) {
      dp[i] = dp[j] * dp[i - j];
    }
  }
};
