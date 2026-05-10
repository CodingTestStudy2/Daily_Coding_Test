'''
1. 아이디어 :
    완전 탐색으로 풀면 시간 초과가 난다.
    지피티한테 물어보니까 병합정렬 기법이 있다고 해서 병합정렬 기법으로 풀었다.
2. 시간복잡도 :
    O(n log n)

3. 자료구조/알고리즘 :
    병합정렬
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        lst = []
        ans = 0
        for num in nums:
            lst.append([num])

        while True:
            tmp = []
            # print('lst:', lst)
            for i in range(0,len(lst) - 1,2):
                left = 0
                right = 0
                l_lst = lst[i]
                r_lst = lst[i+1]
                
                while True:
                    # print('l_lst, r_lst, left, right, ans:', l_lst, r_lst, left, right,ans)

                    if right == len(r_lst):
                        left += 1
                        ans += right
                    elif l_lst[left] > 2 * r_lst[right]:
                        right +=1
                    else:
                        left +=1
                        ans += right

                    # ans += right
                    
                    if left >= len(l_lst):
                        break
                
                s_lst = l_lst + r_lst
                s_lst.sort()
                tmp.append(s_lst)
            
            if len(lst) % 2 != 0:
                tmp.append(lst[len(lst) - 1])
            lst = tmp
            if len(lst) == 1:
                break
                    
        return ans