/**
 * @param {number[]} start
 * @param {number[]} target
 * @return {boolean}
 */
var canReach = function (start, target) {
  const dirs = [
    [-1, -2],
    [-2, -1],
    [-2, 1],
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
  ];
  const visited = Array(8);
  for (let i = 0; i < 8; i++) {
    visited[i] = Array.from({ length: 8 }, () => Array(2));
  }
  const startX = start[0];
  const startY = start[1];
  const queue = [[startX, startY, true]];
  let head = 0;
  visited[startX][startY][1] = true;

  while (queue.length - head > 0) {
    const [curX, curY, curFlag] = queue[head++];
    if (curX === target[0] && curY === target[1] && curFlag) return true;
    for (const [dirX, dirY] of dirs) {
      const nextX = dirX + curX;
      const nextY = dirY + curY;
      const nextFlag = !curFlag;

      if (nextX < 0 || nextY < 0 || nextX >= 8 || nextY >= 8) continue;
      if (visited[nextX][nextY][nextFlag === true ? 1 : 0]) {
        continue;
      }
      visited[nextX][nextY][nextFlag === true ? 1 : 0] = true;
      queue.push([nextX, nextY, nextFlag]);
    }
  }
  return false;
};
