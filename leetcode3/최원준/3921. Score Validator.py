#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''


class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ans = [0,0]
        for event in events:
            if event == "W":
                ans[1]+=1
                if ans[1] == 10:
                    break
            elif event == "WD" or event=="NB":
                ans[0]+=1
            else:
                ans[0] += int(event)
        return ans