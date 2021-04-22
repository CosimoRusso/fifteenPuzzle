class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)