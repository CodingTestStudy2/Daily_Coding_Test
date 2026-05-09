'''
1. 아이디어 :
    평균값을 구해서 그걸 기준으로 팰린드롬을 만들어보고, 
    그 팰린드롬과의 차이를 구해서 최소값을 구한다.
2. 시간복잡도 :

3. 자료구조/알고리즘 :
'''
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        int_avg = int(avg)
        str_avg = str(int_avg)

        left = ''
        
        # len = 9 4개
        for i in range(len(str_avg) // 2):
            left += str_avg[i]
        
        print(left)

        mid = str_avg[len(str_avg) // 2]
        print("mid:",mid)
        print("str_avg:",str_avg)
        print("avg:", avg)

        full_lst = []
        if not left:
            full_lst.append(mid)
            full_lst.append(str(int(mid)+1))
            full_lst.append(str(int(mid)-1))
        else:
            for _str in [left, str(int(left) -1), str(int(left)+1)]:
                if len(str_avg) % 2 != 0:
                    full = _str + mid + _str[-1]
                else:
                    full = _str + _str[-1]
                
                full_lst.append(full)

        # print(full_lst)

        answers = []
        for pan in full_lst:
            ans =0
            for i in nums:
                ans += abs(int(pan) - i)
            answers.append(ans)

        return min(answers)