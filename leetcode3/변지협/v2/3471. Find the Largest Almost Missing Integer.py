'''
1. 아이디어 :
k만큼의 부분배열을 만들고, 부분배열에 포함되는 갯수 센다.

2. 시간복잡도 :
O(n*k)

3. 자료구조/알고리즘 :
'''
from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(int)
        for i in range(n-k+1):
            sub = nums[i:i+k]
            st = set()
            for j in sub:
                st.add(j)
            for j in st:
                dic[j] += 1

        print(dic)
        
        try: 
            return max([key for key,value in dic.items() if value == 1])
        except:
            return -1