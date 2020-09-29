from pprint import pformat, pprint


class TrieNode:
    def __init__(self, value, isComplete=False):
        self.children = {}
        self.value = value
        self.isComplete = isComplete

    def __repr__(self):
        return pformat(self.children)


class Trie:

    def __init__(self):
        self.root = TrieNode("")


    def add(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
            
    def insert(self, word):
        word = word.lower()
        current_node = self.root
        length = len(word) - 1
        for index, char in enumerate(word):
            if char not in current_node.children:
                prefix = word[0:index+1]
                current_node.children[char] = TrieNode(prefix
                ) if index != length else TrieNode(prefix, True)
            current_node = current_node.children[char]
    
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
        


    def get_words(self, prefix):
        prefix = prefix.lower()
        node, exists = self.get_prefix(prefix)
        words = []
        self.get_words_from_node(node, words)
        return words

    def get_words_from_node(self, node, words):
        if node.isComplete:
            words.append(node.value)
        for char in node.children:
            self.get_words_from_node(node.children[char], words)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("Apple")
    trie.insert("All")
    trie.insert("Apps")
    trie.insert("Ape")
    trie.insert("Soda")
    pprint(trie.root.children)
    pprint(trie.get_words("Ap"))
