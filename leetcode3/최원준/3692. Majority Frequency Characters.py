#

'''
1. 아이디어 :
- 알파벳 갯수 카운트
- 카운트가 같은 알파뱃들 모음(freq_dict)
- freq_dict에서 알파뱃 갯수가 더 높으면 교체
- freq_dict에서 알파뱃 갯수가 같으면 카운트 비교 후 더 크면 교체

2. 시간복잡도 :
    O(n + n + n)

3. 자료구조/알고리즘 :
해시맵

'''

from collections import defaultdict
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)
        freq_dict = defaultdict(list)

        for char, freq in counts.items():
            freq_dict[freq].append(char)

        ans = ""
        max_freq = 0
        
        for freq, char_list in freq_dict.items():
            if len(char_list) > len(ans):
                ans = "".join(char_list)
                max_freq = freq
            elif len(char_list) == len(ans):
                if freq > max_freq:
                    ans = "".join(char_list)
                    max_freq = freq
            
        return ans
