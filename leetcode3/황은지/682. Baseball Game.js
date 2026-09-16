/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
  const stack = [];
  for (const op of operations) {
    const len = stack.length;
    if (op === "D") {
      const x = stack[len - 1];
      stack.push(+x * 2);
    } else if (op === "+") {
      const x = stack[len - 1];
      const y = stack[len - 2];
      stack.push(+x + +y);
    } else if (op === "C") stack.pop();
    else stack.push(+op);

    console.log(stack);
  }

  let result = 0;
  for (const num of stack) {
    result += num;
  }

  return result;
};
