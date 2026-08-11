/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function (num) {
  const binary = num.toString(2);
  return parseInt(
    binary
      .split("")
      .map((digit) => (digit === "1" ? "0" : "1"))
      .join(""),
    2,
  );
};
