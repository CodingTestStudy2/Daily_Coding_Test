/**
 * @param {number} n
 * @param {number} s
 * @return {number}
 */
var largestInteger = function(n, s) {
    if(s>9*n) return -1;
    let result=0;
    let rest=s;
    let jisoo=n-1;

    while(rest>0){
        const num=rest<=9? rest:9
        result += ((10**jisoo)*num)
        rest -= num;
        jisoo--;
    }
    return result;

}