class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    """Binary search tree"""
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert_node(self.root, new_val)

    def search(self, find_val):
        return self._search_node(self.root, find_val)

    def print_tree(self):
        return self._preorder_print(self.root, "")[:-1]   # Remove a "- from the end

    def _insert_node(self, start, new_val):
        if start:
            if new_val < start.value:
                if start.left:
                    self._insert_node(start.left, new_val)
                else:
                    start.left = Node(new_val)

            elif new_val > start.value:
                if start.right:
                    self._insert_node(start.right, new_val)
                else:
                    start.right = Node(new_val)
            else:
                # This practice implementation assumes no duplicate values
                raise Exception("Error: tried to insert that is already present in the binary search tree")
        else:
            self.root = Node(new_val)

    def _search_node(self, start, find_val):
        if start:
            if find_val == start.value:
                return True
            elif find_val < start.value:
                return self._search_node(start.left, find_val)
            else:   # find_val > start.value:
                return self._search_node(start.right, find_val)
        else:
            return False

    def _preorder_print(self, start, traversal):
        if start:
            traversal += "{}-".format(start.value)
            traversal = self._preorder_print(start.left, traversal)
            traversal = self._preorder_print(start.right, traversal)
        return traversal

if __name__ == '__main__':
    # Set up tree
    """
        4
       / \
      2   5
     / \
    1   3
    """
    tree = BST(4)
    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))

    # Pre order depth first search print
    print("pre-order DFS traverse:", tree.print_tree())