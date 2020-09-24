from collections import defaultdict
from pprint import pformat, pprint


class TrieNode:
    def __init__(self, isComplete=False):
        self.children = {}
        self.isComplete = isComplete

    def __repr__(self):
        return pformat(self.children)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()
        current_node = self.root
        index = 0
        length = len(word)
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(
                ) if index else TrieNode(False)
            current_node = current_node.children[char]
            index += 1


if __name__ == "__main__":
    trie = Trie()
    trie.insert("Apple")
    trie.insert("All")
    trie.insert("Apps")
    trie.insert("Ape")
    trie.insert("Soda")
    pprint(trie.root.children)
