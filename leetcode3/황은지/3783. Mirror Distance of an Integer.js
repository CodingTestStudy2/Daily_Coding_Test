/**
 * @param {number} n
 * @return {number}
 */
var mirrorDistance = function (n) {
  const revStr = String(n).split("").reverse().join("");
  return Math.abs(n - Number(revStr));
};
