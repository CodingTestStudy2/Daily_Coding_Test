class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        new_sentence = ''
        arr = sentence.split(" ")
        for s in arr:
            replaced=False
            for word in dictionary:
                if s.startswith(word):
                    new_sentence += word
                    replaced=True
                    break

            if not replaced:
                new_sentence += s
            new_sentence += ' '

        return new_sentence.rstrip()
