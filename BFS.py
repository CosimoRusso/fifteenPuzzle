from SearchProblem import SearchProblem
import numpy as np
from Tree import Tree
from Game import Game

class BFS(SearchProblem):
    def solve(self):
        frontier = []
        root = Tree(self.initial_state_)
        frontier.append(root)
        i = 0
        while True:
            node = frontier.pop(0)
            game = node.root
            if self.already_visited(game):
                continue
            else:
                self.mark_as_visited(game)
            i += 1
            if i % 50000 == 0:
                print(i)
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
                frontier.append(new_node)
            # print(game)
            # input()