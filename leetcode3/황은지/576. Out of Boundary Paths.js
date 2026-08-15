/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function (m, n, maxMove, startRow, startColumn) {
  const queue = [[startRow, startColumn]];
  let head = 0;
  let count = 0;
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  for (let i = 0; i < maxMove; i++) {
    const size = queue.length - head;
    for (let k = 0; k < size; k++) {
      const [currR, currC] = queue[head++];
      for (let j = 0; j < 4; j++) {
        const nextR = currR + dir[j][0];
        const nextC = currC + dir[j][1];
        if (nextR < 0 || nextR >= m || nextC < 0 || nextC >= n) count++;
        else queue.push([nextR, nextC]);
      }
    }
  }

  return count % (Math.pow(10, 9) + 7);
};
