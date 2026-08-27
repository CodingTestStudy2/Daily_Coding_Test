class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min_dist = float("inf")
        ans_idx = -1
        tx, ty = target

        for idx, (x, y, r) in enumerate(drones):
            cal_dist = abs(x - tx) + abs(y - ty)

            if cal_dist <= r:
                if cal_dist < min_dist:
                    min_dist = cal_dist
                    ans_idx = idx

        return  ans_idx