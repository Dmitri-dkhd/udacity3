#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


class TrieNode:
    def __init__(self):
        self.node = None
        self.is_word = False
        self.children = {}
        # Initialize this node in the Trie

    def insert(self, char):
        # Add a child node in this Trie
        if not self.node:
            self.node = self.children

        new_char = self.node
        if self.is_word == False:
            new_char[char] = {'word end': False}
        else:
            new_char[char] = {'word end': True}
        new_char = new_char[char]
        self.node = self.node[char]

    def suffixes(self):
        # Recursive function that collects the suffix for
        # all complete words below this point
        
        prefix = self.children
        suffix_set = set()
        if not prefix:
            return None
        def get_suffix(prefix, suffix=''):

            for i in prefix:

                if len(i) > 1:
                    continue

                suffix += i

                if prefix[i]['word end'] == True:
                    suffix_set.add(suffix)

                get_suffix(prefix[i], suffix)
                suffix = suffix[:-1]

        get_suffix(prefix)
        return suffix_set


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        self.root.node = self.root.children
        for index, char in enumerate(word):
            
            if index == len(word)-1:
                self.root.is_word = True
                
                if self.root.node.get(char):
                    self.root.node['word end'] = True
                    continue
            else:
                self.root.is_word = False
            
            if self.root.node.get(char):
               
                self.root.node = self.root.node[char]
                continue

            self.root.insert(char)
            
        self.root.node = None

    def find(self, prefix):
        current_char = self.root.children
        current_node = TrieNode()
        for char in prefix:
            if current_char.get(char):
                current_char = current_char[char]
            else:
                return None
        current_node.children = current_char
        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:




# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[3]:


MyTrie=Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[4]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


prefixNode = MyTrie.find('a')#['nt', 'nthology', 'ntagonist', 'ntonym']
print(prefixNode.suffixes())

prefixNode = MyTrie.find('')#['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
print(prefixNode.suffixes())


for i in range(200):
    MyTrie.insert(str(i))


prefixNode = MyTrie.find('1') # all ints from 0 to 199 starting with '1' 
print(prefixNode.suffixes())

