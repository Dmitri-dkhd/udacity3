Dictionaries where used to structure the Trie because of the fast lookups and the chaining possibility.

RouteTrieNode.insert in the Node takes constant time and space.
RouteTrieNode.__init__ takes time and space complexity is O(1).

RouteTrie.__init__ takes time and space complexity is O(1).
RouteTrieNode.insert takes time and space complexity is O(n) traversing with a recursive approach thought a Trie out of  dictionaries. 
The RouteTrie.find method traverses the Trie with a loop, takes time complexity of O(n) and space complexity of O(1).

Router.add_handler() inserts the path in the router and sets the handler.
Router.add_handler() takes time and space complexity is O(1) as it is traversing with a recursive approach thought a Trie with the insert() method. 

Router.lookup() uses RouteTrie.find to check if the path is in the router and return the handler or the error handler. Takes time complexity of O(n) and space complexity of O(1).

Router.split_path() takes time complexity of O(n) and space complexity of O(n).  because of the The split() method.

The overall time and space complexity is O(n) (n= the splitted path).