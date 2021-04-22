from Game import Game
from BFS import BFS

def main():
    game = Game(3)
    print(game)
    print("Solving...")
    bfs = BFS()
    bfs.initial_state(game)
    solution = bfs.solve()
    [print(s) for s in solution]

if __name__ == '__main__':
    main()