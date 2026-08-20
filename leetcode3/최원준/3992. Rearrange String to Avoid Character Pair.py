#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        counter = Counter(s)

        ans = ""
        if y in counter:
            ans += y*counter[y]
        if x in counter:
            ans += x*counter[x]
        for char, freq in counter.items():
            if char == x or char == y:
                continue
            ans += char * freq
        return ans
