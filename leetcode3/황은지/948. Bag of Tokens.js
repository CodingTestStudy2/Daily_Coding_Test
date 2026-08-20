/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function (tokens, power) {
  const dp = Array(10000);
  dp[power] = 0;
  const queue = [[power, 0]];
  let head = 0;
  let maxScore = 0;

  while (queue.length - head > 0) {
    const [curP, curS] = queue[head++];
    maxScore = Math.max(maxScore, curS);

    for (const token of tokens) {
      if (curP >= token) queue.push([curP - token, curS + 1]);
      if (curS >= 1) queue.push([curP + token, curS - 1]);
    }
  }
};
