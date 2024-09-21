# Ordered: Yes (in terms of character sequence)
# Mutable: Yes
# Duplicates: No (keys are unique in terms of their paths)
# Indexing: No (typically accessed via traversal)
# Different Data Types: Yes (nodes hold characters or other data)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Check if any word in the trie starts with the given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Create a trie and perform operations
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")

print(trie.search("apple"))      # Output: True
print(trie.search("app"))        # Output: True
print(trie.search("appl"))       # Output: False
print(trie.starts_with("app"))   # Output: True
print(trie.starts_with("appl"))  # Output: True
print(trie.starts_with("banana"))# Output: False
