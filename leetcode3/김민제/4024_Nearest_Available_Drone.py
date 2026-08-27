import sys

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        answer = sys.maxsize
        answer_arr = []
        answer_i = []
        for i,num in enumerate(drones):
            temp = abs(num[0]-target[0])+abs(num[1]-target[1])
            if temp <= num[2]:
                answer = min(answer,temp)
                answer_arr.append(answer)
                answer_i.append(i)
        if not answer_i:
            return -1
        else:
            return answer_i[answer_arr.index(min(answer_arr))]


drones = [[4,4,5]]
target = [8,6]

#drones = [[2,1,5],[4,4,5],[6,6,8]]
#target = [5,5]

solution = Solution()
print(solution.nearestDrone(drones,target))
