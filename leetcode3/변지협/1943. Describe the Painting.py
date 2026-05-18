'''
1. 아이디어 :
    그냥 전체 딕셔너리 다 돌려고 했었는데 시간초과 난다.
    딕셔너리 전체 돌지 말고 각 구간에서 +, - 따지는 방식으로 구현
2. 시간복잡도 :
    O(n log n)
3. 자료구조/알고리즘 :
    차분배열
'''

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for x1,x2,n in segments:
            dic[x1] += n
            dic[x2] -= n
        
        print(dic)

        dic = dict(sorted(dic.items(), key=lambda x: x[0]))

        keys = [key for key in dic.keys()]
        last = 0
        
        ans = []
        for i in range(len(keys) - 1):
            last += dic[keys[i]]
            if last:
                ans.append([keys[i],keys[i+1],last])

        return ans