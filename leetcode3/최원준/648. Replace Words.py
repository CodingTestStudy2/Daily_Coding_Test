from collections import defaultdict

class Node:
    def __init__(self):
        self.children = {}
        self.word = None

#

'''
1. 아이디어 :
각 단어를 매칭할때 시간복잡도가 터질 수 있다(sentance 단어 1000개, 단어의 길이 1000, dictionary의 단어 1000)
trie 자료 구조를 만들어서 매칭 시간을 줄인다.

2. 시간복잡도 :
    O(a * b + c * d) dictionary.length:a, dictionary.word.length: b, sentence.words:c, word.length:d

3. 자료구조/알고리즘 :
trie

'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Node()

        def insert_word(word, index, node):
            if index >= len(word):
                node.word = word
                return
            char = word[index]
            if char not in node.children:
                child_node = Node()
                node.children[char] = child_node
            else:
                child_node = node.children[char]
            insert_word(word, index+1, child_node)
        
        def search_word(word, index, node):
            if index >= len(word):
                return word
            char = word[index]
            if node.word != None:
                return node.word
            if char not in node.children:
                return word
            child_node = node.children[char]
            return search_word(word, index+1, child_node)        
        
        for word in dictionary:
            insert_word(word, 0, trie)

        words = sentence.split(" ")
        for i in range(len(words)):
            words[i] = search_word(words[i], 0, trie)
        
        return " ".join(words)
        
        
