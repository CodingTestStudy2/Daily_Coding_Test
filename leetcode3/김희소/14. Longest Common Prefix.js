/**
 * @param {string[]} strs
 * @return {string}
 */

 // 인덱스 0의 단어를 기준으로 잡고 그 다음 단어와 겹치는 글자들이 있으면 킾해놓고 다음꺼에 그게 있는지 비교하고...?

var longestCommonPrefix = function(strs) {
    const list = [];
    for ( let i=1; i<strs.length; i++) {
        let temp = "";
        for (let j=0; j<strs[0].length; j++) {
            if (strs[0][j] == strs[i][j]) {
                temp += strs[0][j];
            }
        }
        list.push(temp)
    }
    return list.reduce((a,b) => a.length <= b.length ? a : b)
};