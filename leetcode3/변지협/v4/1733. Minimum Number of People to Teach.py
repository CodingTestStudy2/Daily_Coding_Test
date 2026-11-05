from collections import defaultdict
class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        tmp = []
        for a,b in friendships:
            tmp.append((a-1,b-1))
        
        dic = defaultdict(list)
        
        for a,b in tmp:
            a_lan = set(languages[a])
            b_lan = set(languages[b])

            overlap = a_lan & b_lan
            if not overlap:
                dic[a].append(b)
                dic[b].append(a)
        
        print(dic)

        for i in range(n):
            most_freq = defaultdict(int)
            for friend in dic[i]:
                for j in languages[i]:
                    most_freq[j] += 1

            most_freq = sorted(most_freq.items(), key=lambda x:x[1], reverse=True)
            
            for key,value in most_freq:
                

            print(most_freq)

            
                
