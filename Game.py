import numpy as np

class Game():
    def __init__(self, size, initial_grid=None):
        self.size = size
        self.max_tile = pow(size, 2)
        if initial_grid is None:
            self.grid = np.arange(1, size*size+1)
            rng = np.random.default_rng()
            rng.shuffle(self.grid)
            self.grid = self.grid.reshape((size, size))
        else:
            self.grid = initial_grid

    def move(self, direction):
        num = self.max_tile
        pos_i, pos_j = np.where(self.grid == num)
        new_pos_i = pos_i
        new_pos_j = pos_j
        if direction == 'UP':
            new_pos_i = pos_i - 1
        elif direction == 'LEFT':
            new_pos_j = pos_j - 1
        elif direction == 'BOTTOM':
            new_pos_i = pos_i+1
        elif direction == 'RIGHT':
            new_pos_j = pos_j + 1
        else:
            raise Exception("%s is an invalid direction" % direction)
        k = self.grid[new_pos_i, new_pos_j]
        self.grid[new_pos_i, new_pos_j] = num
        self.grid[pos_i, pos_j] = k

    def get_possible_moves(self):
        num = self.max_tile
        i, j = np.where(self.grid == num)
        out = []
        if i > 0:
            out.append("UP")
        if i < self.size - 1:
            out.append("BOTTOM")
        if j > 0:
            out.append("LEFT")
        if j < self.size - 1:
            out.append("RIGHT")
        return out

    def finished(self):
        return (np.reshape(self.grid, self.max_tile) == np.arange(1, self.max_tile+1)).all()

    def duplicate(self):
        return Game(self.size, np.copy(self.grid))

    def get_misplaced_tiles(self):
        final_grid = np.array(np.arange(1, self.max_tile+1)).reshape((self.size, self.size))
        differences = sum((((self.grid - final_grid) != 0) * 1).reshape(self.max_tile))
        return differences

    def manhattan_distance(self):
        final_grid = np.arange(1, self.max_tile+1).reshape((self.size, self.size))
        man_dist = 0
        for i in range(self.size):
            for j in range(self.size):
                cell = self.grid[i, j]
                x, y = np.where(final_grid == cell)
                x, y = (x[0], y[0])
                man_dist += abs(x - i) + abs(y - j)
        return man_dist


    def is_solvable(self):
        grid = self.grid.reshape(self.max_tile)
        inversions = 0
        for i in range(len(grid)):
            if grid[i] == 9:
                continue
            for j in range(i+1, len(grid)):
                inversions += (grid[i] > grid[j]) * 1
        max_tile_row, max_tile_col = np.where(self.grid == self.max_tile)
        return (self.size % 2 == 1 and inversions % 2 == 0) or \
               (self.size % 2 == 0 and inversions % 2 == 1 and max_tile_row % 2 == 0) or \
                (self.size % 2 == 0 and inversions % 2 == 0 and max_tile_row % 2 == 1)



    def __str__(self):
        out = ""
        for row in self.grid:
            for c in row:
                padding = 4 if self.size > 3 else 3
                num = ' ' if c == pow(self.size, 2) else c
                out += ("%s" % num).center(padding) + '|'
            out += '\n'
        return out


if __name__ == '__main__':
    g1 = Game(3)
    print(g1)
    print(g1.manhattan_distance())