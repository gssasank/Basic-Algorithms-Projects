# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, page):
        self.children[page] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.head = RouteTrieNode()

    def insert(self, path):
        paths = split_path(path)
        current_node = self.head
        for i in paths:
            if i not in current_node.children:
                current_node.insert(i)
            current_node = current_node.children[i]

    def find(self, path):
        paths = split_path(path)
        current_node = self.head
        for i in paths:
            if i not in current_node.children:
                return None
            current_node = current_node.children[i]
        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, head_handler):
        self.head = RouteTrieNode()
        self.head_handler = head_handler

    def add_handler(self, path, handler_data):
        paths = self.split_path(path)
        current_node = self.head
        for page in paths:
            if page not in current_node.children:
                current_node.insert(page)
            current_node = current_node.children[page]
        current_node.handler = handler_data

    def lookup(self, path):
        if path == "/":
            return "root handler"
        paths = self.split_path(path)
        current_node = self.head
        for i in paths:
            try:
                if current_node.children[i]:
                    current_node = current_node.children[i]
                else:
                    return None
            except:
                return None
        return current_node.handler

    def split_path(self, path):
        if path[0] == "/":
            path = path[1:]

        elif path[-1] == "/":
            path = path[:-1]

        paths = path.split("/")

        return paths


router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
