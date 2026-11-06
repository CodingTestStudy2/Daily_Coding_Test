class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        def count_diff(base_word, to_word):
            n = len(base_word)
            count = 0
            for i in range(n):
                if base_word[i] != to_word[i]:
                    count+=1
            return count
        
        def count_max_diff(word):
            max_diff = 3
            for dic_word in dictionary:
                max_diff = min(max_diff, count_diff(word, dic_word))
            return max_diff <= 2
        
        ans = []
        for query in queries:
            if count_max_diff(query):
                ans.append(query)
        return ans
