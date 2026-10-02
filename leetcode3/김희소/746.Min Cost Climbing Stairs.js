/**
 * @param {number[]} cost
 * @return {number}
 */

// 계단을 오르는데 드는 최소 비용을 구하는 문제,
// 시작 지점 : 인덱스 0 또한 인덱스 1

// 인덱스 0 혹은 1을 골랐을 때의 각각 최소비용을 비교해서 정해야?

var minCostClimbingStairs = function(cost) {
    const minCost = [];

    if (cost.length === 2) {
        return Math.min(...cost)
    }

    minCost[0] = cost[0];
    minCost[1] = cost[1];

    for (let i = 2; i < cost.length; i++) {
        minCost[i] = Math.min(minCost[i -1], minCost[i - 2]) + cost[i];
    }
    
    return Math.min(
        minCost[cost.length -1],
        minCost[cost.length -2]
    )
};