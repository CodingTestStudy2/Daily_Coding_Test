'''
실패
'''
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        st = set()
        lst = []
        for num in nums:
            if num in st:
                lst.append(0)
            else:
                if num % 2 == 0:
                    lst.append(1)
                else:
                    lst.append(-1)

            st.add(num)

        ans = []
        tmp2 = []

        for i in lst:
            tmp = []
            for value, length in ans:
                tmp.append((value + i, length + 1))

            tmp.append((i, 1))
            ans = tmp
            tmp2.extend(ans)

        try:
            return max([length for value, length in tmp2 if value == 0 and not (value == 0 and length == 1)])
        except:
            return 0
