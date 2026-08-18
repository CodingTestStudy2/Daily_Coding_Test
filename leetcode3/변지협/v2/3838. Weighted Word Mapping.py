
'''
1. 아이디어 :
alphabet dic, dic_rev 만들고, 이에 매핑해서 구한다.

2. 시간복잡도 :
    o(n * m) n: words 길이, m: word 길이
3. 자료구조/알고리즘 :
'''
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        dic = {}
        dic_rev = {}
        wn = len(weights)
        for i in range(wn):
            dic[alphabet[i]] = weights[i]
            dic_rev[25-i] = alphabet[i]
        
        ans = ''
        for word in words:
            tmp = sum([dic[w] for w in word])
            ans += dic_rev[tmp%26]
        
        return ans
        
            