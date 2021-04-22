from SearchProblem import SearchProblem

class a_star(SearchProblem):
    def cost_function(self, node):
        return node.cost_until_now + node.cost_to_goal