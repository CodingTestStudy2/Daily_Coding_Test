/**
 * @param {string} s
 * @return {number}
 */
var countValidPrefixes = function(s) {
    let zeroCount=0;
    let oneCount=0;
    let result=0;

    for(const digit of s){
        if(digit==="0") zeroCount++
        else oneCount++;

        if(Math.abs(zeroCount-oneCount)<=1) result++; 
    }

    return result;
};