from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        set_order = set(char for char in order)
        counter = defaultdict(int)
        remain = ""

        for char in s:
            if char in set_order:
                counter[char]+=1
            else:
                remain += char

        ans = ""
        for char in order:
            ans += char * counter[char]
        return ans + remain
