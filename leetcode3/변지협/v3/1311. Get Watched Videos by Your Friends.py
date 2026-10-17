'''
1. 아이디어 :
    id에서 출발해 BFS를 돌면서 거리(level)를 함께 큐에 저장한다.
    거리가 level인 친구들을 모은 뒤, 그 친구들이 본 영상들을 세어서
    (시청 횟수, 제목) 오름차순으로 정렬해 반환한다.
2. 시간복잡도 :
   o(V + E + N log N) — 그래프 탐색 V+E, 영상 정렬 N log N
3. 자료구조/알고리즘 :
   BFS, defaultdict, Counter

'''

from collections import defaultdict, deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        n = len(friends)
        friend_map = defaultdict(list)
        for i, friend in enumerate(friends):
            friend_map[i].extend(friend)

        visited = [False] * n
        queue = deque()
        queue.append((0, id))
        visited[id] = True

        levels = []
        while queue:
            i, current = queue.pop()

            if i == level:
                levels.append(current)
            else:
                for nxt in friend_map[current]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append((i + 1, nxt))

        ans = []
        for i in levels:
            for j in watchedVideos[i]:
                ans.append(j)

        return [key for key, value in sorted(Counter(ans).items(), key=lambda x: (x[1], x[0]))]
