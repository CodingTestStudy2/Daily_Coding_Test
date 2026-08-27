/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function (arr) {
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    let min = Infinity;
    for (let j = i; j < arr.length; j++) {
      min = Math.min(min, arr[j]);
      sum = (sum + min) % (Math.pow(10, 9) + 7);
    }
  }

  return sum;
};

// // a b c d
// a ab abc abcd
// b bc bcd
// c cd
// d

// // a b
// a<b
// a+b+a

// a>b
// a+b+b

// // a b c
// a<b<c
// a + b + c
// a+ a+
// b+
