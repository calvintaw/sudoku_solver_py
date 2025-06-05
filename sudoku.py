import time

class Board:
    def __init__(self, board):
        self.board = board
        self.err_count = 0
    
    def __str__(self):
        result = ""
        
        for row in self.board:
            nums = " | ".join(str(x) for x in row)
            result += f"{nums}\n{"-" * len(nums)}\n"
                    
        return result
    
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                index = contents.index(0)
                return row, index
            except ValueError:
                pass
        return None
            
    def valid_in_col(self, col, num):
        for row in self.board:
            if num == row[col]:
                return False
        return True
    
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_square(self, row, col, num):
        row_index = (row // 3) * 3
        col_index = (col // 3) * 3
        
        for row in range(row_index, row_index + 3):
            for col in range(col_index, col_index + 3):
                if num == self.board[row][col]:
                    return False
        return True
    
    def is_valid(self, row, col, num):
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        
        return all([valid_in_col, valid_in_row, valid_in_square])
    
    def solve(self):
        if self.find_empty_cell() is None:
            return True
        row, col = self.find_empty_cell()    
            
        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.board[row][col] = i 
                   
                if self.solve():
                    return True 
                       
        self.board[row][col] = 0
        self.err_count += 1
        return
                
            
def play_sudoku(puzzle):
    gameboard = Board(puzzle)
    start = time.perf_counter()
    if gameboard.solve():
        duration = (time.perf_counter() - start)
        print(f"Solved the puzzle. Time: {duration:.4f}s Error Count: {gameboard.err_count}")
    else:
        print("Failed to solve puzzle")
    print(gameboard)
        
puzzle_3 = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

puzzle_1 = [
    [4, 8, 0, 3, 2, 0, 7, 5, 6],
    [9, 7, 0, 8, 5, 0, 1, 2, 4],
    [0, 2, 6, 7, 1, 4, 0, 3, 8],
    [7, 6, 0, 4, 0, 8, 3, 1, 2],
    [1, 0, 0, 0, 0, 0, 4, 8, 5],
    [0, 4, 0, 5, 3, 1, 0, 0, 9],
    [0, 0, 0, 6, 0, 5, 8, 4, 0],
    [8, 1, 0, 9, 0, 2, 0, 0, 3],
    [6, 0, 0, 1, 8, 0, 2, 9, 0]
]

puzzle_2 = [
    [2, 0, 7, 0, 0, 8, 6, 1, 0],
    [5, 3, 0, 4, 0, 0, 7, 0, 2],
    [1, 6, 4, 9, 7, 2, 0, 0, 8],
    [0, 7, 0, 6, 9, 0, 2, 0, 0],
    [0, 0, 9, 0, 2, 0, 0, 4, 0],
    [0, 2, 3, 0, 4, 0, 0, 7, 6],
    [0, 0, 2, 0, 8, 0, 4, 5, 0],
    [0, 0, 6, 7, 0, 9, 8, 0, 1],
    [7, 8, 0, 2, 1, 4, 0, 6, 0]
]



if __name__ == "__main__":
    play_sudoku(puzzle_2)