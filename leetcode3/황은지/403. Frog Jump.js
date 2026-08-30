/**
 * @param {number[]} stones
 * @return {boolean}
 */
var canCross = function(stones) {
    const dp =Array.from({length:stones.length},()=>Array(3).fill(false));
    dp[1][1]=true;

// 길이는 전길이에 따라 달라짐
    for(let i=0;i<stones.length-1;i++){
        const pos=stones[i];
        for(let j=0;j<3;j++){
            if(dp[i][j]===true){
            } 
        }
    }

    return  true;
};