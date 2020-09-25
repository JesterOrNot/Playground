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
        length = len(word) - 1
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(
                ) if index != length else TrieNode(True)
            current_node = current_node.children[char]
            index += 1
    
    def get_prefix(self, prefix):
        prefix_exists = False
        index = 0
        prefix = prefix.lower()
        length = len(prefix) - 1
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                current_node = None
                break
            if index == length:
                prefix_exists = True
            current_node = current_node.children[char]
            index += 1
        return (current_node, prefix_exists)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("Apple")
    trie.insert("All")
    trie.insert("Apps")
    trie.insert("Ape")
    trie.insert("Soda")
    pprint(trie.root.children)
