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

    def solve(self):
        pass