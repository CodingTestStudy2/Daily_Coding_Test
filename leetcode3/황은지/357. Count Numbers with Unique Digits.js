/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function (n) {
  // n=1 0~9 모두가능
  // n=2 0~99 두개 겹치는거 (9가지) 빼고 가능
  // n=3 0~999 세개 겹치는거(9가지)+두개 겹치는거(9가지) 빼고 가능
  // n=2일때 케이스 + 세자리수에서 겹치는거 뺀것
  const dp = Array(n + 1);
  dp[0] = 1;
  if (n >= 1) dp[1] = 10;

  for (let i = 2; i <= n; i++) {
    dp[i] = 10 * dp[i - 1] - (n - 1) * 9;
    //100~999 중 겹치는거 뺀것
    //100~199  dp[i-1]-2
    //200~299   dp[i-1] -2
    // 900~999 ...
  }

  return dp[n];
};
