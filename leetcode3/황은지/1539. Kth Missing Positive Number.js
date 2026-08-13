/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    const set=new Set(arr);

    let count=0;

    for(let i=1;i<=100000;i++){
        if(!set.has(i)){
            count++;
            if(count===k) return i;
        }
    }
};