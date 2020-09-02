'''
A clearer way to build a trie with a Python default dictionary.
Trienode class is using collections.defaultdict instead of a normal dictionary.
'''

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = None

# Implement the add and exists function using the new TrieNode class
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        # Append word to trie
        pass
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        # Check if word exists in trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert word_trie.exists('there')
assert not word_trie.exists('zzz')
print('All tests passed!')