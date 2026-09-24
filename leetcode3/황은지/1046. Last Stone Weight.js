// class MaxHeap {
//   constructor() {
//     this.heap = [];
//   }

//   getParentIndex(idx) {
//     return Math.floor((idx - 1) / 2);
//   }

//   getRightChildIndex(idx) {
//     return idx * 2 + 2;
//   }

//   getLeftChildIndex(idx) {
//     return idx * 2 + 1;
//   }

//   hasParent(idx) {
//     return this.getParentIndex(idx) >= 0;
//   }

//     size(){
//         return this.heap.length;
//     }
//   add(val) {
//     this.heap.push(val);
//     this.heapifyUp();
//   }

//   remove() {
//     if (this.heap.length === 0) return null;

//     const top = this.heap[0];
//     this.heap[0] = this.heap[this.heap.length - 1];
//     this.heap.pop();
//     this.heapifyDown();
//     return top;
//   }

//   heapifyUp(val) {
//     let idx = this.heap.length - 1;
//     while (this.hasParent(idx)) {
//       let parentIdx = getParentIndex(idx);
//       if (this.heap[idx] > this.heap[parentIdx]) {
//         this.swap(idx, parentIdx);
//         idx = parentIdx;
//       } else {
//         break;
//       }
//     }
//   }

//   heapifyDown() {
//     let idx = 0;
//     while (this.getLeftChildIndex(idx) > 0) {
//       let largerIdx = this.getLeftChildIndex(idx);
//       if (
//         this.getRightChildIndex(idx) < this.heap.length &&
//         this.heap[this.getRightChildIndex(idx)] < this.heap[largerIdx]
//       ) {
//         largerIdx = this.getRightChildIndex(idx);
//       }
//       if (this.heap[largerIdx] > this.heap[idx]) {
//         this.swap(largerIdx, idx);
//         idx = largerIdx;
//       } else {
//         break;
//       }
//     }
//   }

//   swap(a, b) {
//     [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
//   }
// }

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
  const maxHeap = new MaxHeap();
  for (const stone of stones) {
    maxHeap.push(stone);
  }

  while (maxHeap.size() > 1) {
    const num1 = maxHeap.pop();
    const num2 = maxHeap.pop();
    if (num1 === num2) continue;
    maxHeap.push(Math.abs(num1 - num2));
  }
  if (maxHeap.size() === 0) return 0;
  return maxHeap.pop();
};
