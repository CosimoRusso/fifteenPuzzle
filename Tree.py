class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
        self.parent = None
        self.cost_to_goal = root.manhattan_distance()
        self.cost_until_now = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        child.cost_until_now = self.cost_until_now + 1