class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sorted_dict = sorted(dictionary, key=len)
        pieces = sentence.split()

        print(sorted_dict)
        print(pieces)

        ans = []

        for i in pieces:
            for j in sorted_dict:
                if i.startswith(j):
                    ans.append(j)
                    break
            else:
                ans.append(i)

        return ' '.join(ans)