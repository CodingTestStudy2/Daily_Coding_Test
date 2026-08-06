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

