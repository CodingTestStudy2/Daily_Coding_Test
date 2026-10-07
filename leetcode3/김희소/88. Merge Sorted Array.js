/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

/**
정수 배열 nums1과 nums2가 오름차순(비내림차순) 으로 정렬되어 있고, 정수 m과 n이 주어진다.
- m은 nums1에서 실제로 사용되는 원소의 개수
- n은 nums2의 원소 개수
두 배열을 하나의 오름차순 배열로 합쳐야 한다.
단, 결과 배열을 새로 만들어서 반환하는 것이 아니라, nums1 배열 자체를 수정해서 결과를 저장해야 한다.
이를 위해 nums1의 길이는 m + n이다.
- nums1의 앞쪽 m개 원소는 실제 데이터이다.
- 뒤쪽 n개 원소는 0으로 채워져 있으며, 이 값들은 무시하면 된다.
- 이 공간은 nums2의 원소를 합치기 위해 미리 확보된 공간이다.
- nums2의 길이는 n이다.
 */
var merge = function(nums1, m, nums2, n) {
    nums1.splice(m);
    nums1.push(...nums2)
    nums1.sort((a,b) => a - b);
};