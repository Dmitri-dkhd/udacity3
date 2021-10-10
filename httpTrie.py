# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = None
        self.root_handler=None
    def insert(self, arr, arr_0=None):

        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if not arr_0:
            arr_0 = arr
        if not self.root.node:
            self.root.node = self.root.children
        if self.root.node.get(arr[0]):
            if len(arr) == 1:
                self.root.node[arr[0]]['handler'] = self.handler
                return
            self.root.node = self.root.node[arr[0]]
            return self.insert(arr[1:], arr_0)

        if len(arr) == 1:
            self.root.handler = self.handler
            self.root.insert(arr[0])
            self.root.node = self.root.children
            return

        if len(arr) == len(arr_0):
            self.root.handler = self.root_handler

        self.root.insert(arr[0])
        return self.insert(arr[1:], arr_0)

    def find(self, match):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_path = self.root.children
        for index, element in enumerate(match):

            if current_path.get(element):
                if index == len(match)-1:
                    return current_path[match[-1]]['handler']

                current_path = current_path[element]

            else:
                return None


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.node = None
        self.children = {}
        self.handler = None

    def insert(self, value):
        # Insert the node as before
        if not self.node:
            self.node = self.children
        self.node[value] = {'handler': self.handler}
        self.handler = None
        self.node = self.node[value]


class Router:
    def __init__(self, root_handler, error_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie()
        self.error_handler = error_handler
        self.root_handler = root_handler

    def add_handler(self, path, handler):
        self.route.root_handler = self.root_handler
        self.route.handler = handler
        self.route.insert(self.split_path(path))

        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path)

        if not path:
            return self.root_handler
        if self.route.find(path):
            return self.route.find(path)
        else:
            return self.error_handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[-1] == '/':
            path = path[:-1]
        path = path.split('/')
        return path
# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
router.add_handler("/home/about/read", "read handler")
print(router.lookup("/home/about/read/"))
print(router.lookup("/home/about"))
router.add_handler("/new/waz/home/about/read/magazine", "magazine handler")
print(router.route.root.children)
print(router.lookup("/"))