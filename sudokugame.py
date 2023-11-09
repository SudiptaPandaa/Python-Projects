import tkinter as tk
from tkinter.simpledialog import askinteger

BROWN = "brown"
BLACK = "black"
VIOLET = "violet"
board = [[0 for _ in range(5)] for _ in range(5)]

def get_input():
    for row in range(5):
        for col in range(5):
            value = askinteger("Sudoku Input", f"Enter value for cell ({row+1}, {col+1}):", initialvalue=0)
            if value is not None:
                board[row][col] = value
                update_board()

def update_board():
    canvas.delete("all")
    draw_board()

def draw_board():
    for row in range(5):
        for col in range(5):
            value = board[row][col]
            x = col * 50
            y = row * 50
            canvas.create_rectangle(x, y, x + 60, y + 60, fill=VIOLET, outline=BROWN)
            if value != 0:
                canvas.create_text(x + 20, y + 20, text=str(value), font=("Georgia", 24), fill=BLACK)
root = tk.Tk()
root.title("5x5 Sudoku")
canvas = tk.Canvas(root, width=250, height=250, bg=BLACK)
canvas.pack()
input_button = tk.Button(root, text="Input Values", command=get_input, bg="Orange")
input_button.pack()
draw_board()
root.mainloop()
