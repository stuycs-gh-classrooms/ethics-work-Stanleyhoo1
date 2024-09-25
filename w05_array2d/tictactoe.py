grid = []

game_grid = [['' for _ in range(3)] for _ in range(3)]

game = True
turn = True

def check_win():
    # Check rows and columns
    for i in range(3):
        # Check rows
        if game_grid[i][0] == game_grid[i][1] == game_grid[i][2] != '':
            return game_grid[i][0]
        # Check columns
        if game_grid[0][i] == game_grid[1][i] == game_grid[2][i] != '':
            return game_grid[0][i]
    # Check diagonals
    if game_grid[0][0] == game_grid[1][1] == game_grid[2][2] != '':
        return game_grid[0][0]
    if game_grid[0][2] == game_grid[1][1] == game_grid[2][0] != '':
        return game_grid[0][2]
    # Check for draw
    for row in game_grid:
        if '' in row:
            return None  # Game is not over yet
    return 'Draw'

def create_row_col():
    row = []
    for i in range(17):
        if (i+1)%6!=0:
            row.append('_')
        else:
            row.append('|')
    return row

def create_row():
    row = []
    for i in range(17):
        if (i+1)%6!=0:
            row.append(' ')
        else:
            row.append('|')
    return row

for i in range(9):
    if (i+1)%3==0 and i!=8:
        grid.append(create_row_col())
    else:
        grid.append(create_row())

def display(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()
            
display(grid)

def play_turn():
    global turn
    empty = True
    while empty == True:
        print("Enter the row (0-2): ")
        row = input()
        print("Enter the col (0-2): ")
        col = input()
        if int(col) > 2 or int(row) > 2:
            print("Invalid move! Index out of bounds!")
        if grid[int(row)*3+1][int(col)*5+2+int(col)] == ' ':
            if turn == True:
                grid[int(row)*3+1][int(col)*5+2+int(col)] = 'X'
                game_grid[int(row)][int(col)] = 'X'
            else:
                grid[int(row)*3+1][int(col)*5+2+int(col)] = 'O'
                game_grid[int(row)][int(col)] = 'O'
            turn = not turn
            empty = False
        else:
            print("Spot is already taken!")

while game==True:
    play_turn()
    display(grid)
    result = check_win()
    if result:
        if result == 'Draw':
            print("The game is a draw!")
        else:
            print(f"Player {result} wins!")
        game = False
    