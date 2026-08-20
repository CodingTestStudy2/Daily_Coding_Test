/**
 * @param {string} s
 * @param {character} x
 * @param {character} y
 * @return {string}
 */
var rearrangeString = function(s, x, y) {
   let left=0;
   let right=s.length-1;
   const arr=s.split("");

   while(left<right){
    while(left<arr.length && arr[left]!==x ){left++};
    while(right>=0 && arr[right]!==y){right--};
    if(left>=right) break;
    // swap
    const temp=arr[left];
    arr[left++]=arr[right];
    arr[right--]=temp;
    console.log(arr);
   }

   return arr.join("");
};