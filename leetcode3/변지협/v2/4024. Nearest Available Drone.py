class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        lst = []
        tx,ty = target

        for x,y,r in drones:
            distance = abs(x-tx) + abs(y-ty)
            if distance <= r:
                lst.append(distance)
            else:
                lst.append(99999)
        
        _min = min(lst)
        
        if _min == 99999:
            return -1
        else:
            return lst.index(_min)