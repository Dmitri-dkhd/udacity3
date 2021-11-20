The method Trie.find() traverses through the prefix String and searches through the levels of the Trie until the last character of prefix und returns the corresponding dictionary.
The time complexity is T(word).

Trie.insert uses Trie.find to check if the new word is in the root as part of the saved words and sets the new 'word ends'.
Also insert the new chars to the root.
The time complexity is T(word * word).

TrieNode.suffixes() method appends all possible suffixes of the given
node to a list.
The time complexity is T(n) where n is the number of dicts in the   TrieNode.

The overall time complexity is O(n) for traversing the TrieNode (n = number of dicts) same as the space complexity because of the dict data structure. 