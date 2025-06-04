# Sudoku Solver (Python)

This is a command-line Sudoku solver written in Python. It uses a backtracking algorithm to solve a 9x9 Sudoku puzzle in-place.

I originally built this following instructions from [FreeCodeCamp's Python Sudoku solver exericse from their Scientific Computing with Python course](https://www.youtube.com/watch?v=eqUwSA0xI-s), then rewrote it from scratch a couple of days later to reinforce what I learned

---

## How It Works

The solver uses a **recursive backtracking algorithm** to fill the board one empty cell at a time. For each empty cell, it tries digits 1–9 and checks whether placing the digit would be valid:

- It must **not already exist** in the same row.
- It must **not already exist** in the same column.
- It must **not already exist** in the same 3x3 square.

If no digit fits, the function backtracks to the previous cell and tries a different number. This continues until the puzzle is solved or deemed unsolvable.

## Problem I Ran Into

While rewriting the solver, I initially **forgot to include the recursive return** inside the `solve()` method and **Unfortunately I had to ask Chatgpt to give me hints TWICE**.
I only realised what I needed to do after ChatGPT said "What should the function do if a valid recursive solution is found"
:

```python
if self.solve():
    return True
```

```python
    def solve(self):
        if self.find_empty_cell() is None:
            return True
        row, col = self.find_empty_cell()

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.board[row][col] = i

                # added the above code here to make the code work
                #{--------------}
        self.board[row][col] = 0
        return
```

---

## 💻 Running the Solver

The main code is in a single Python file. To run:

```bash
python sudoku.py
```
