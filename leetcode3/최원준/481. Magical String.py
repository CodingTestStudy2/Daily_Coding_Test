#

'''
1. 아이디어 :
_next가 가리키는 값(1 또는 2)을 현재 숫자 num을 몇 번 붙일지로 사용.
처음에는 고정 start [1, 2]를 읽어서 1, 22를 만들고, 이후부터는 만들어진 s 자신을 읽는다.
num은 매번 1 → 2 → 1 → 2로 바꾸고, s 길이가 n이 되면 1의 개수를 센다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''
class Solution:
    def magicalString(self, n: int) -> int:
        # 1 22 11 2 1 22 1 22 11 2 11 22
        # 1 22 11 2 1 22 1 22
        # 1 22 11 2 1 2
        # 1 22 11
        # 1 22
        # 1 2
        
        s = []
        start = [1, 2]

        _next = 0
        num = 1

        while len(s) < n:
            if _next < len(start):
                count = start[_next]
            else:
                count = s[_next]

            for _ in range(count):
                s.append(num)
                if len(s) == n:
                    break
                # print(s)
            
            num = 3 - num
            _next += 1
        return s.count(1)
        


