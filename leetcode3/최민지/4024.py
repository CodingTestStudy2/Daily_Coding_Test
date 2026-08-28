class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        result = []
        for drone in drones:
            s = drone[0]
            e = drone[1]
            r = drone[2]
            temp = abs(s - target[0]) + abs(e - target[1])
            if  temp <= r:
                result.append(temp)
            else: 
                result.append(100)
        

        output = min(result)
        if output != 100:
            return result.index(output)
        else:
            return -1
            