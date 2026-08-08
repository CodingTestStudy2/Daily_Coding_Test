'''
1. 아이디어 :
각 order에 있는 문자를 dictionary에 숫자로 넣고, 이 숫자로 s에 있는 문자를 치환한 후
이 문자들을 정렬을 수행한다. 다시 dictionary2에 숫자를 문자로 치환해서 ans에 넣는다.

2. 시간복잡도 :
    O(nglon)

3. 자료구조/알고리즘 :
'''
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dic = {}
        dic2 = {}
        n = len(order)
        
        for i in range(n):
            dic[order[i]] = i+1
            dic2[str(i+1)] = order[i]
        
        print(dic)

        ans = ''
        tmp = []
        
        for _s in s:
            if _s in dic:
                tmp.append(str(dic[_s]))
            else:
                ans += _s
        
        tmp = [int(i) for i in tmp]
        tmp.sort()
        print(tmp)

        for t in tmp:
            ans += dic2[str(t)]

        # print(ans)

        return ans