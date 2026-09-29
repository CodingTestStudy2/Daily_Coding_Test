/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  const countMap = new Map();

  for (const char of s) {
    countMap.set(char, (countMap.get(char) || 0) + 1);
  }

  for (const char of t) {
    const count = countMap.get(char);
    if (count === 0 || count === undefined) return false;
    countMap.set(char, count - 1);
  }
  return true;
};
