
from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: list[list[str]],
        friends: list[list[int]],
        id: int,
        level: int
    ) -> list[str]:

        queue = deque([id])
        visited = {id}

        for _ in range(level):
            for _ in range(len(queue)):
                person = queue.popleft()

                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)

        count = Counter()

        for person in queue:
            count.update(watchedVideos[person])

        return sorted(count, key=lambda video: (count[video], video))
