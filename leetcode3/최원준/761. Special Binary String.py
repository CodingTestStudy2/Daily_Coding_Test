#

'''
1. 아이디어 :
조건들은:
  - 무조건 1로 시작
  - 1과 0의 갯수가 같아야한다
  - 0의 갯수는 1의 갯수보다 커지는 경우는 없어야한다.
special_string(ss)는 재귀적으로도 special string입니다.
예시에서 
11011000의 갯수는 (1은 +1, 0은 -1)일때, 12123210 입니다.
ss이기떄문에 1 101100 0으로 나눕니다.
재귀적으로 1 + makeLargestSpecial(101100) + 0으로 재귀적으로 내려갈 수 있고,
101100의 갯수는 101210 입니다.
0이 되는순간 나눕니다. 10, 1100으로 나눠지고 이는 다시
1 + makeLargestSpecial("") + 0, 1 + makeLargestSpecial(10) + 0 이 됩니다.
이는 [1 + "" + 0, 1 + 10 + 0]이 되고, 이를 정렬하면 [1100, 10]이며, 정렬된걸 합쳐서(110010) 리턴합니다.
그러면 다시 올라가서 (1 + makeLargestSpecial(101100) + 0)
1 + 110010 + 0이 됩니다.

2. 시간복잡도 :
    O(nlogn)

3. 자료구조/알고리즘 :
재귀

'''

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        balance = 0
        nums = []
        temp = ""

        for c in s:
            if c == "1":
                balance +=1
                temp += c
            else:
                balance -=1
                temp += c
            
            if balance == 0:
                nums.append(temp)
                temp = ""
        
        processed = []

        for num in nums:
            mid = num[1:-1]
            largest_special = "1" + self.makeLargestSpecial(num[1:-1]) + "0"
            processed.append(largest_special)

        processed.sort(reverse=True)
        return "".join(processed)

        

        
        
