from sortedcontainers import SortedList
from Tree import Tree

class SearchProblem():
    def __init__(self):
        self.initial_state_ = None
        self.visited_states = {}

    def mark_as_visited(self, state):
        self.visited_states[str(state)] = True

    def already_visited(self, state):
        return str(state) in self.visited_states

    def initial_state(self, initial_state):
        self.initial_state_ = initial_state

    def actions(self, state):
        return state.get_possible_moves()

    def apply_action(self, state, action):
        state.move(action)

    def objective_test(self, state):
        return state.finished()

    def step_cost(self):
        return 1

    def cost_function(self, node):
        pass

    def solve(self):
        frontier = SortedList(key=lambda k: self.cost_function(k))
        root = Tree(self.initial_state_)
        frontier.add(root)
        i = 0
        while (True):
            len(frontier) == 0 and print("FRONTIER EMPTY AFTER %d ITERATIONS" % i)
            node = frontier.pop(0)
            game = node.root
            if self.already_visited(game):
                continue
            else:
                self.mark_as_visited(game)
            i += 1
            if i % 50000 == 0:
                print("iterations: %d, frontier: %d" % (i, len(frontier)))
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
                frontier.add(new_node)