import tkinter as tk

CELL_SIZE = 40
GRID_ROWS = 10
GRID_COLS = 10

def main():
    def on_mouse_move(event):
        # Move the eraser
        canvas.coords(eraser, event.x - 20, event.y - 20, event.x + 20, event.y + 20)

        # Check collision with each cell
        for cell in cells:
            x1, y1, x2, y2 = canvas.coords(cell)
            ex1, ey1, ex2, ey2 = canvas.coords(eraser)

            # Check if eraser overlaps with cell
            if not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2):
                canvas.itemconfig(cell, fill='white')

    # Set up window and canvas
    root = tk.Tk()
    root.title("Canvas Eraser")
    canvas = tk.Canvas(root, width=GRID_COLS * CELL_SIZE, height=GRID_ROWS * CELL_SIZE, bg='white')
    canvas.pack()

    # Create grid of blue rectangles (cells)
    cells = []
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            rect = canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
            cells.append(rect)

    # Create the eraser rectangle
    eraser = canvas.create_rectangle(0, 0, 40, 40, outline='red')

    # Bind mouse movement to erasing action
    canvas.bind('<Motion>', on_mouse_move)

    root.mainloop()

if __name__ == '__main__':
    main()
