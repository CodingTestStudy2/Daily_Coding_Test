/**
 * @param {string} s
 * @return {number}
 */
var vowelConsonantScore = function (s) {
  let v = 0;
  let c = 0;
  for (const char of s) {
    if (
      char === "a" ||
      char === "e" ||
      char === "i" ||
      char === "o" ||
      char === "u"
    )
      v++;
    else if (char !== " " && isNaN(char)) c++;
  }

  return c > 0 ? Math.floor(v / c) : 0;
};
