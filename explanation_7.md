Dictionaries where used to structure the Trie because of the fast lookups and the chaining possibility.

RouteTrieNode.insert in the Node takes constant time and space.
RouteTrieNode.__init__ takes time and space complexity is O(1).

RouteTrie.__init__ takes time and space complexity is O(1).
RouteTrieNode.insert takes time and space complexity is O(n) traversing with a recursive approach thought a Trie out of  dictionaries. 
(With self.root.node.get() takes time and space complexity is O(1).
 self.root.insert() takes time and space complexity is O(1).)

The RouteTrie.find method traverses the Trie with a loop, takes time complexity of O(n) and space complexity of O(1).
(With   current_path.get(element) takes time and space complexity is O(1) and self.split_path(path) takes time complexity of O(n) and space complexity of O(n))

 

Router.add_handler() inserts the path in the router and sets the handler.
Router.add_handler() takes time and space complexity is O(n) as it is traversing with a recursive approach thought a Trie with the insert() method. 
(With self.route.insert takes time and space complexity is O(n))

Router.lookup() uses RouteTrie.find to check if the path is in the router and return the handler or the error handler. Takes time complexity of O(n) and space complexity of O(1).
(With self.split_path(path) takes time complexity of O(n) and space complexity of O(n).
self.route.find(path) takes time complexity of O(n) and space complexity of O(1).)

Router.split_path() takes time complexity of O(n) and space complexity of O(n).  because of the The split() method.

The overall time and space complexity is O(n) (n= the splitted path).