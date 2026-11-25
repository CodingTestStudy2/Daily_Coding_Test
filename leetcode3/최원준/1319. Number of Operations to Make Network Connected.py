class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        
        connection_map = defaultdict(list)

        for x, y in connections:
            connection_map[x].append(y)
            connection_map[y].append(x)

        networks = 0
        visited = set()

        def bfs(computer):
            visited.add(computer)
            queue = deque()
            queue.append(computer)

            while queue:
                computer = queue.popleft()
                for neighbor in connection_map[computer]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)

        for i in range(n):
            if i not in visited:
                bfs(i)
                networks+=1

        return networks-1
