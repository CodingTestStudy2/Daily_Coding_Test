class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        def is_diff_one(str1,str2):
            o = len(str1)
            same_num = 0
            for i in range(o):
                if str1[i] == str2[i]:
                    same_num +=1
            
            return same_num + 1 == o
        
        ans = 0
        for i in range(n):
            for j in range(i,n):
                s_part = s[i:j+1]
                for k in range(m-(j-i)):
                    t_part = t[k:k+(j-i+1)]
                    if is_diff_one(s_part,t_part):
                        ans +=1

        return ans                    