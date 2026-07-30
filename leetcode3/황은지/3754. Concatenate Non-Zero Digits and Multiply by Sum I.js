/**
 * @param {number} n
 * @return {number}
 */
var sumAndMultiply = function (n) {
  const numStr = String(n);
  let sum = 0;
  let x = "";

  for (const ch of numStr) {
    if (ch !== "0") {
      sum += Number(ch);
      x += ch;
    }
  }
  return sum * Number(x);
};
