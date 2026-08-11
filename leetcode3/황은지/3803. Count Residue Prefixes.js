/**
 * @param {string} s
 * @return {number}
 */
var residuePrefixes = function(s) {
    // residue: prefix중, 서로 다른 문자의 길이가 전체 길이를 3으로 나눈 나머지일때
    
    let count=0;
    const set=new Set();

    for(let i=0;i<s.length;i++){
        set.add(s[i]);
        if((i+1)%3===set.size) count++;
    }

    return count;
};