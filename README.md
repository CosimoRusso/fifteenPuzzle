# Fifteen Game

A python implementation of the fifteen game with solver included.

## Structure

### Game.py
The implementation of the fifteen puzzle game. It is a class that accepts a param, *size*, which defines the size of the grid. for the 15 game, this number is 4, as the grid is a 4x4.

### SearchProblem.py
Abstract class that describes a search problem. All concrete solvers extend this class.

### BFS.py
Solves the game using Breadth First Search.

### Greedy.py
Solves the game using a greedy approach, 
