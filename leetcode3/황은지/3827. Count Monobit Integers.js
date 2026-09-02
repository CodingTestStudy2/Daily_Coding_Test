/**
 * @param {number} n
 * @return {number}
 */
var countMonobit = function(n) {
    // 0은 꼭 포함, 나머지는 전부 1로만 이루어짐
    let count=1;
    const binary=n.toString(2);
    count+=(binary.length-1);
    if(!binary.includes("0")) count+=1;

    return count;
};