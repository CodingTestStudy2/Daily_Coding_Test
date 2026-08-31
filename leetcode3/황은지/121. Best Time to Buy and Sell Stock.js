/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max=0;
    let maxProfit=0;
    for(let i=prices.length-1;i>=0;i--){
        max=Math.max(max,prices[i]);
        maxProfit=Math.max(maxProfit,max-prices[i]);
    }

    return maxProfit;
};