from bisect import bisect_left
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []


    def addNum(self, value: int) -> None:
        idx = bisect_left(self.intervals, [value, value])


        # 이미 포함되어 있는 경우
        if idx > 0 and self.intervals[idx - 1][0] <= value <= self.intervals[idx - 1][1]:
            return


        # 왼쪽 구간과 연결되는 경우
        if idx > 0 and self.intervals[idx - 1][1] + 1 == value:
            self.intervals[idx - 1][1] = value

            # 왼쪽과 확장 후 오른쪽과도 연결되는 경우
            if idx < len(self.intervals) and self.intervals[idx][0] == value + 1:
                self.intervals[idx - 1][1] = self.intervals[idx][1]
                self.intervals.pop(idx)

            return


        # 오른쪽 구간과 연결되는 경우
        if idx < len(self.intervals) and self.intervals[idx][0] - 1 == value:
            self.intervals[idx][0] = value
            return


        # 새로운 구간 추가
        self.intervals.insert(idx, [value, value])


    def getIntervals(self) -> List[List[int]]:
        return self.intervals