'''
alternating?

00101
0 : valid
00 : invalid
001 : 010 /valid
0010 : 0100 invalid
00101 : 10101 : valid

00000111

01010100
0의개수와 1의 개수가 같거나
0의 개수가 1의 개수보다 한개더 많거나
111 00
10101
'''
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        answer_count=0
        for num in range(len(s)):
            temp = s[0:num+1]
            count_0 = temp.count('0')
            count_1 = temp.count('1')

            if abs(count_0-count_1)==1 or count_0 == count_1:
                answer_count+=1
                
        return answer_count
        
