class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
            
        counter1 = Counter(s)
        counter2 = Counter(t)

        for char1, freq in counter1.items():
            if counter2[char1] != freq:
                return False
        return True
