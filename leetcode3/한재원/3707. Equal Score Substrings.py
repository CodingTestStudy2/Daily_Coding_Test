'''
input: string of alphabet letters
output: boolean - if the string can be split into substrings with equal scores

- each alphabet has the score a=1... z=26

- make dictionary key: a-z, value: 1-26
- two pointer 
        adcb
        |  |
    - while check current point of each pointer
        - if left > right
            move right pointer to the left
        - else 
            move left pointer to the right
        - return if the score is equal
    - return false

TC: O(N), SC: O(26) - O(1)

'''
class Solution:
    def scoreBalance(self, s: str) -> bool:
        score_dict = {}
        
        for i in range(26):
            score_dict[chr(ord('a') + i)] = i + 1
        
        total = 0
        
        for ch in s:
            total += score_dict[ch]
        
        left = 0
        
        for i in range(len(s) - 1):
            left += score_dict[s[i]]
            right = total - left
            
            if left == right:
                return True
        
        return False