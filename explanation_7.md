add_handler() inserts the path in the router and sets the handler.
add_handler( has time and space complexity of RouteTrie.insert.

lookup() uses find() to check if the path is in the router and return the handler or the error handler. Has same complexity as find().

Insert in the Node takes constant time and space.

Inserting in the Router/RouteTrie takes linear time and also space as it is traversing with a recursive approach thought a Trie out of  dictionaries. 

Dictionaries where used to structure the Trie because of the fast lookups and the chaining possibility.

The split() method in split_path() takes also linear time and space.


The lookup and find methods traverses the Trie with a loop, takes also linear time and constant space.

The overall time and space complexity is O(n) n= the splitted path as also in find(path).