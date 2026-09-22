/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function (bills) {
  const billCount = Array(5).fill(0);

  for (const bill of bills) {
    let change = bill - 5;
    if (change !== 0) {
      for (let i = 4; i >= 0; i--) {
        if (billCount[i] === 0) continue;
        const curBil = i * 5;
        while (billCount[i] * curBil >= change) {}
        if (curBil >= change) {
          const total = curBil * billCount[i];
          if (total >= change) change === 0;
          else {
            change -= billCount[i] * curBil;
            billCount[i] = 0;
          }
        }
        if (change === 0) break;
      }
      if (change > 0) return false;
    }
    billCount[bill / 5]++;
    console.log(billCount);
  }
  return true;
};
