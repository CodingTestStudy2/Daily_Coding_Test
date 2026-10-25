class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        '''
        12345678901
        0112
         00001112
             00012

        12345678901
        00001112
            0112
             00012

        12345678901
        00012
           00001112
               0112

        1. growTime이 짧을 수록 마지막으로 간다.
        2. growTime이 길수록 제일 앞으로 간다.
        '''
        n = len(plantTime)
        types = [[plantTime[i], growTime[i]] for i in range(n)]
        types.sort(key=lambda x: -x[1])

        max_time = 0
        next_day = 0
        for plant_time, grow_time in types:
            plant_day = next_day
            next_day += plant_time

            max_time = max(max_time, plant_day + plant_time + grow_time)
        return max_time
