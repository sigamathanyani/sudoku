import random

class Sudoku:
    def __init__(self):
        self.board = [[random.randint(1,9) for col in range(9)] for row in range(9)]
