/**
 * @param {number} n
 * @return {boolean}
 */
var consecutiveSetBits = function (n) {
  const binary = n.toString(2);
  let hasPair = false;
  for (let i = 1; i < binary.length; i++) {
    if (binary[i] === "1" && binary[i - 1] === "1") {
      if (hasPair) return false;
      hasPair = true;
    }
  }
  return hasPair;
};
