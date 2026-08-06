'''
1. 아이디어 :
prefix에 있는 단어를 완전 탐색으로 찾아서 바꾸는 형태로 진행한다.
for i in lst 이렇게 하면 시간 초과 나는데
for i in dic 이렇게 하면 시간 초과가 안난다.
왜냐하면 dic은 해시맵이기 때문에 검색 시간이 o(1)이 걸리고, lst는 리스트기 때문에 검색 시간이 o(n)이 걸린다.

2. 시간복잡도 :
    o(n^2)

3. 자료구조/알고리즘 :
완전탐색
'''
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        ans = []
        dic = {}
        for d in dictionary:
            dic[d] = 0
        
        for sen in sentence.split():
            tmp = ''
            for s in sen:
                tmp += s
                if tmp in dic:
                    break

            ans.append(tmp)

        ans2 = ''
        for an in ans:
            ans2 += an + ' '
        
        return ans2[:len(ans2)-1]

