import random
from sudoku import Board, play_sudoku;


class SudokuGenerator(Board):
    def __init__(self, difficulty = 100):
        self.board = self.generate_empty_grid()
        self.generate_board()
        self.left_to_remove = difficulty
        
    def __str__(self):
        output = ""
        
        for row in self.board:
            result = " | ".join([str(x) for x in row])
            output += f"{result}\n{"-" * len(result)}\n"
            
        return output
    
    def generate_empty_grid(self):
        return [[0 for j in range(9)] for i in range(9)]
            
    def generate_board(self):
        position = self.find_empty_cell()
        
        if (position) is None:
            return True
        
        row, col = position
        
        tried_values = set()
        
        while len(tried_values) < 9:  
            num = random.randint(1, 9)
            
            while num in tried_values:
                num = random.randint(1, 9)
            
            if self.is_valid(row, col, num):
                self.board[row][col] = num
            
                if self.generate_board():
                    return True
            tried_values.add(num)
            
        self.board[row][col] = 0
        return                
        
    def _remove_cell(self, row, col):
        pass
        
    def create_puzzle(self):
        if self.left_to_remove <= 0:
            return
        row, col = (random.randint(0, 8), random.randint(0, 8))
        
        while self.board[row][col] == 0:
            row, col = (random.randint(0, 8), random.randint(0, 8))
            
        self.board[row][col] = 0
            
        if self.solve():
            self.left_to_remove -= 1
            self.create_puzzle()
        
        self.board[row][col] = 0
        
                    
        
def generateAndsolve():
    
    board = SudokuGenerator(random.randint(50, 100))
    board.create_puzzle()
    print("Puzzle: ")
    print(board)
    play_sudoku(board.board)
    

if __name__ == "__main__":
    generateAndsolve()