class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ans = [0,0]
        for event in events:
            if event in ["0","1","2","3","4","6"]:
                ans[0] += int(event)
            elif event == "W":
                ans[1] += 1
            elif event in ["WD","NB"]:
                ans[0] += 1

            if ans[1] == 10:
                break

        return ans