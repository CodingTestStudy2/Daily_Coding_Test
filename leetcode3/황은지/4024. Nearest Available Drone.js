/**
 * @param {number[][]} drones
 * @param {number[]} target
 * @return {number}
 */
var nearestDrone = function (drones, target) {
  let min = Infinity;
  let minIndex;

  const targetX = target[0];
  const targetY = target[1];

  for (let i = 0; i < drones.length; i++) {
    [x, y, range] = drones[i];
    const dist = Math.abs(x - targetX) + Math.abs(y - targetY);
    if (dist > range) continue;
    if (dist < min) {
      min = dist;
      minIndex = i;
    }
  }

  return min === Infinity ? -1 : minIndex;
};
