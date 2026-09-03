
'''
1. 아이디어 :
두개를 정렬하고, 스택에 넣어 비교하면서 꺼내서 dictionary에 정리한다.

2. 시간복잡도 :
o(n logn - 정렬)

3. 자료구조/알고리즘 :
'''

from collections import defaultdict

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp1 = sorted(nums1)[::-1]
        tmp2 = sorted(nums2)[::-1]
        tmp_lst = []
        dic = defaultdict(list)
        ans = []

        print(tmp1)
        print(tmp2)

        while True:
            if not tmp1:
                break
            
            if tmp1[-1] > tmp2[-1]:
                t1 = tmp1.pop()
                t2 = tmp2.pop()
                dic[t2].append(t1)
            else:
                t1 = tmp1.pop()
                tmp_lst.append(t1)
        
        print(dic, tmp_lst)

        for i in nums2:
            # print(i,dic)
            if i in dic and dic[i]:
                ans.append(dic[i].pop())
            else:
                t = tmp_lst.pop()
                ans.append(t)
        
        return ans