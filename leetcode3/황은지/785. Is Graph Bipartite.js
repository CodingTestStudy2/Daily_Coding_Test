/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function (graph) {
  const nodeCount = graph.length;
  const setFlag = Array(nodeCount);
  const queue = [0];
  setFlag[0] = true;
  let head = 0;

  while (queue.length - head > 0) {
    const curNode = queue[head++];
    console.log(curNode, "curNode");
    for (let i = 0; i < graph[curNode].length; i++) {
      const nextNode = graph[curNode][i];
      console.log(nextNode, "nextNode");
      if (setFlag[nextNode] === setFlag[curNode]) return false;
      setFlag[nextNode] = !setFlag[curNode];
      queue.push(nextNode);
    }
  }

  return true;
};
