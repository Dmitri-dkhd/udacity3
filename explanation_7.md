Dictionaries where used to structure the Trie because of the fast lookups and the chaining possibility.

RouteTrieNode.insert in the Node takes constant time and space.
RouteTrieNode.__init__ takes constant time and space.

RouteTrie.__init__ takes constant time and space.
RouteTrieNode.insert takes linear time and also space as it is traversing with a recursive approach thought a Trie out of  dictionaries. 
The RouteTrie.find methods traverses the Trie with a loop, takes also linear time and constant space.

Router.add_handler() inserts the path in the router and sets the handler.
Router.add_handler() takes linear time and also space as it is traversing with a recursive approach thought a Trie with the insert() method. 

Router.lookup() uses RouteTrie.find to check if the path is in the router and return the handler or the error handler. Takes also linear time and constant space.

Router.split_path() takes also linear time and space  because of the The split() method.

The overall time and space complexity is O(n) (n= the splitted path).