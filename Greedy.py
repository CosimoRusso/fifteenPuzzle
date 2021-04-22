from SearchProblem import SearchProblem
from Tree import Tree
from sortedcontainers import SortedList

class Greedy(SearchProblem):
    def cost_function(self, node):
        return node.cost_to_goal