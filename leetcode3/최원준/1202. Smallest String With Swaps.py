from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        s = list(s)

        dic = defaultdict(list)

        for i1, i2 in pairs:
            dic[i1].append(i2)
            dic[i2].append(i1)

        visited = set()

        for i in range(n):
            if i in visited:
                continue

            stack = [i]
            visited.add(i)
            indexes = []

            while stack:
                cur = stack.pop()
                indexes.append(cur)

                for nxt in dic[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)

            chars = sorted(s[j] for j in indexes)
            indexes.sort()

            for idx, char in zip(indexes, chars):
                s[idx] = char

        return "".join(s)
