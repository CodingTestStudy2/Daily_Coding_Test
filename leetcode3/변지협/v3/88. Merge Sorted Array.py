'''
1. 아이디어 :
    nums1은 앞 m개가 실제 값이고 뒤쪽은 0으로 채워진 여유 공간이다.
    nums1의 앞 m개만 잘라내고 nums2의 앞 n개를 이어 붙인 뒤 정렬하면 두 배열이
    합쳐진 정렬 결과가 된다. 결과를 nums1에 그대로 반영해야 하므로 리스트
    객체를 바꾸지 않고 슬라이스 대입(nums1[:] = merged)으로 덮어쓴다.

2. 시간복잡도 :
    o((m+n) log(m+n))  (정렬)

3. 자료구조/알고리즘 :
    리스트, 정렬

'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = nums1[:m]
        nums2 = nums2[:n]

        merged.extend(nums2)
        merged.sort()
        nums1[:] = merged
