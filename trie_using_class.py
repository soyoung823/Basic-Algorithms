'''
Trie: a new type of Tree

Build a software that provides spell check feature.
This software will only say if the word is valid or not.
It doesn't give suggested words.
From the knowledge you've already learned, how would you build this?

The simplest solution is to have a hashmap of all known words.
It would take O(1) to see if a word exists, but the memory size would be O(n*m),
where n is the number of words and m is the length of the word.

Let's see how a Trie can help decrease the memory usage while sacrificing a little on performance.
'''

# Basic Trie
'''
Let's look at a basic Trie with the following words: 'a', 'add', and 'hi'
'''

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False}, 
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}
    }

print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))

def is_word(word):
    '''
    look for the word in 'basic_trie'
    '''
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]
    return current_node['word_end']

# Test words
test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('{} is a word.'.format(word))
    else:
        print('{} is not a word.'.format(word))


# Trie using a class
'''
Just like most tree data structure, 
let's use classes to build th Trie.
Implement two functions for the Trie class below.
Implement add to add a word to the Trie.
Implement exists to return True if the word exist in the trie and False if the word doesn't exist in the trie.

'''
class TrieNode(object):

    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        # Append 'word' to trie
        
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
        cur_node.is_word = True
        
    def exists(self, word):
        # Check if word exists in trie
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        return cur_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('{} is a word.'.format(word))
    else:
        print('{} is not a word.'.format(word))