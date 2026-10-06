/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str = s.replace(/[^a-z0-9]/gi, "").toLowerCase();
    let reversed = str.split('').reverse().join('')
    return str === reversed ? true : false
};