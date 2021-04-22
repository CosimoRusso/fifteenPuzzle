from Game import Game
from Greedy import Greedy
from BFS import BFS
from a_star import a_star
import numpy as np
from datetime import datetime

def main():
    size = 4
    game = Game(size)
    while not game.is_solvable():
        game = Game(size)
    # print(game)
    # print("Solving...")
    start_time = datetime.now()
    solver = Greedy()
    # solver = BFS()
    # solver = a_star()
    solver.initial_state(game)
    solution = solver.solve()
    [print(s) for s in solution]
    tot_time = datetime.now() - start_time
    print("Time [s]: %.3f" % (tot_time.microseconds / 1e6))

if __name__ == '__main__':
    main()