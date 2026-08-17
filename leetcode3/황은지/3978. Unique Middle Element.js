/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMiddleElementUnique = function(nums) {
    const middleIndex=Math.floor(nums.length/2);
    const middleNum=nums[middleIndex];

    for(let i=0;i<nums.length;i++){
        if(i===middleIndex) continue;
        if(nums[i]===middleNum) return false;
    }
    return true;
};