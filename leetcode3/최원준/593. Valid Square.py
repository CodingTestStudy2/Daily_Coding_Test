class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        
        def get_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x1-x2) ** 2 + (y1-y2) ** 2
        
        points=[p1,p2,p3,p4]
        distances = []

        for i in range(4):
            for j in range(i+1, 4):
                distances.append(get_distance(points[i], points[j]))
        
        distances.sort()

        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5]
            and distances[4] == 2 * distances[0]
        )
