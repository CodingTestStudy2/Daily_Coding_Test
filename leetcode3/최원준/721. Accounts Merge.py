#

'''
1. 아이디어 :
dictionary 하나로는 같은 key가 존재하여 관리가 안됩니다.
key: [set1, set2, ...]식으로 관리를 합니다.

2. 시간복잡도 :
    O(1000 * (10 + 1000))

3. 자료구조/알고리즘 :
dict, set

'''
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        map = defaultdict(list)
        
        for account in accounts:
            name = account[0]
            emails = set(account[1:])

            overlap_set = []
            
            for email_set in map[name]:
                if emails & email_set:
                    overlap_set.append(email_set)
            
            if not overlap_set:
                map[name].append(emails)
                continue
            
            for email_set in overlap_set:
                emails.update(email_set)
                map[name].remove(email_set)
            
            map[name].append(emails)
        
        ans = []
        for name, email_sets in map.items():
            for email_set in email_sets:
                ans.append([name] + sorted(email_set))
        
        return ans

