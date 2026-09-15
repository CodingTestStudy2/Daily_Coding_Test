/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const dp=Array(n+1).fill(0);
    dp[0]=1;
    for(let i=0;i<n;i++){
        if(i<n) dp[i+1]+=dp[i];
        if(i<n-1) dp[i+2]+=dp[i];
    }

    return dp[n];


};