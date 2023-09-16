import random

class Sudoku:
    def __init__(self):
        self.board = []
        self.generate_board()
        print(self.board)

    def check_valid_move(self,board,x,y,number):
        #check for x - direction
        if number in board[y]:
            return False
        
        #check for y - direction
        for y in range(9):
            if number == board[y][x]:
                return False

        #check for a 3x3 block
        start_y, start_x = 3 * (y // 3), 3 * (x // 3)
        for y in range(start_y, start_y + 3):
            for x in range(start_x, start_x + 3):
                if board[y][x] == number:
                    return False
        
        return True
    
    def generate_board(self):
        new_row = [0,0,0,0,0,0,0,0,0]
        already_out = []
        value = random.randint(1,9)

        for idx in range(9):  
            while value in already_out:
                value = random.randint(1,9)

            already_out.append(value)
            new_row[idx] = value
            self.board.append(new_row)
            new_row = [0,0,0,0,0,0,0,0,0]
            idx+=1
            
        
        for y in range(9):
            for x in range(9):
                num = random.randint(1,9)
                valid_move = self.check_valid_move(self.board,x,y,num)
                if valid_move and self.board[y][x] == 0:
                    self.board[y][x] = num
                    


