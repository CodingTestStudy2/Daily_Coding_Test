/**
 * @param {number[]} nums
 * @return {number}
 */
var alternatingSum = function(nums) {
    let result=0;

    for(let i=0;i<nums.length;i++){
        if(i%2===0) result+=nums[i];
        else result-=nums[i];
    }

    return result;
};