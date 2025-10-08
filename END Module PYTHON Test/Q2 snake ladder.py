import random

# Board size (10x10)
rows, cols = 10, 10

# Total cells
total = rows * cols

# Generate 7 random snake heads (excluding 1 and 100)
snake_heads = random.sample(range(2, total), 7)

# Create board
board = []

# Fill board from 100 → 1 (like real snake & ladder board)
num = total
for r in range(rows):
    row = []
    for c in range(cols):
        if num in snake_heads:
            row.append(f"{num:2}>:")
        else:
            row.append(f"{num:2}")
        num -= 1
    # Reverse every second row to create zig-zag layout
    if r % 2 == 1:
        row.reverse()
    board.append(row)

# Display board
for r in board:
    print(" ".join(r))
