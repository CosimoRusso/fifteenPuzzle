from SearchProblem import SearchProblem
from Tree import Tree
from collections import deque

class Greedy(SearchProblem):
    def cost_function(self, node):
        return node.cost_to_goal

    def solve(self):
        frontier = {}
        size = self.initial_state_.size
        for i in range((size * 2 - 2) * pow(size, 2)):
            frontier[i] = deque()
        root = Tree(self.initial_state_)
        frontier[root.cost_to_goal].append(root)
        i = 0
        while (True):
            # len(frontier) == 0 and print("FRONTIER EMPTY AFTER %d ITERATIONS" % i)
            node = None
            for key in frontier:
                if len(frontier[key]) > 0:
                    node = frontier[key].pop()
                    break
            game = node.root
            if self.already_visited(game):
                continue
            else:
                self.mark_as_visited(game)
            i += 1
            if i % 50000 == 0:
                print("iterations: %d, frontier: %s" % (i, str([len(frontier[k]) for k in frontier])))
            if game.finished():
                out = []
                current = node
                while current.parent is not None:
                    out.append(current)
                    current = current.parent
                out.append(current)
                out.reverse()
                return [n.root for n in out]
            successors = self.actions(game)
            for s in successors:
                new_game = game.duplicate()
                self.apply_action(new_game, s)
                new_node = Tree(new_game)
                node.add_child(new_node)
                frontier[new_node.cost_to_goal].append(new_node)