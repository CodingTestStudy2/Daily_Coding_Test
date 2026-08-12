/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    if(deck.length===1) return false;

    const numCount = {};
    for (const num of deck) {
        numCount[num] = (numCount[num] || 0) + 1;
    }

    const counts = Object.values(numCount);

    let totalGcd=counts[0];
    
    const gcd=(a,b)=>{
        return b===0? a:gcd(b,a%b);
    }

    for(let i=1;i<counts.length;i++){
        totalGcd=gcd(totalGcd,counts[i]);
        if(totalGcd===1) return false;
    }

    return totalGcd>=2
};