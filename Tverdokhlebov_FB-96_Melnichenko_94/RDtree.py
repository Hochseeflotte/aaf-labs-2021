
from pptree import *

class Element:
    def __init__(self, value: set):
        self.left = None
        self.data = value
        self.right = None
class RDtree:
    root = None
    def get_element_data(self, data):
        return Element(data)
    def insert(self, element, data: set):
        if not element:
            return self.get_element_data(data)
        self.root = element

        if not self.is_child(element):
            if len(element.left.data.intersection(data)) > len(element.right.data.intersection(data)):
                element.data = element.data.union(data)
                self.insert(element.left, data)
            else:
                element.data = element.data.union(data)
                self.insert(element.right, data)
        else:
            element.left = self.get_element_data(element.data)
            element.data = element.data.union(data)
            element.right = self.get_element_data(data)
        return element

    def is_child(self, element: Element):
        if element.left or element.right:
            return False
        return True

    def tree_to_dict(self, element):
        tree = {}
        def prepare_tree(element):
            if self.is_child(element):
                return tree
            tree[str(element.data)] = {str(element.left.data), str(element.right.data)}
            prepare_tree(element.left)
            prepare_tree(element.right)
        prepare_tree(element)
        tree_dict=tree
        self.print_tree(tree_dict, str(element.data))

    def print_tree(self, tree, root, *, indent=0, criteria=None):
        depth, branch, visited = criteria or (0, [], set())
        if root not in tree:
            return
        if depth == 0:
            print(" " * indent + root)
        visited |={root}
        branch += [None]
        fork=len(set(tree[root]) - visited)
        for visited_elem in sorted(set(tree[root]) - visited):
            fork -=1
            branch[depth] = ("├──" if fork else "└──")
            if visited_elem in visited: continue
            print(" " * indent + "".join(branch) + visited_elem)
            if visited_elem in tree:
                branch[depth]=("│   "if fork else "    ")
                new_creteria = depth+1, branch.copy(),visited.copy()
                self.print_tree(tree,visited_elem, indent=indent, criteria= new_creteria)
