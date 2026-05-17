
'''
1. 아이디어 :
    이중 for문 돌려야하는데 ages length로 for문 돌리면 시간초과남.
    age는 1-120이므로 120으로 for문 돌려서 dic에서 개수 가져와서 계산하면됨.
2. 시간복잡도 :
    O(120*120)
3. 자료구조/알고리즘 :
'''

'''
0.5 * age[x] + 7 < age[y] <= age[x] and

age[y] <= 100 or age[x] >= 100

이면 보낸다.
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dic = defaultdict(int)
        
        for age in ages:
            dic[age] += 1
        
        print(dic)

        answer = 0
        for x,v in dic.items():
            for y,v2 in dic.items():
                # print(x,y)
                send = True
                if y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100):
                    send = False
                
                # print("x,y,send:", x,y,send)
                # print(send)

                if send:
                    if x == y:
                        answer += v * (v2 - 1)
                    else:
                        answer+= v * v2

        return answer