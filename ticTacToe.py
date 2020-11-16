
# 1. TicTacToe
state = [[0,0,0,],[0,0,0],[0,0,0]]
where = (1,1)
xory = "X"
print(f'\nState before move\n{state}')
def move(board,location,player):
    if (len(board) != 3) or (len(board[0]) != len(board[1]) != len(board[2] != 3)):
        return print("The board is the wrong size!")
    elif 2 < location[0] or 2 < location[1] or location[0] < 0 or location[1] < 0:
        return print("Location is invlid")
    elif board[location[0]][location[1]] != 0:
        return print("The location is already occupied")
    elif player not in ["x", "X", "y", "Y"]:
        return print("Player must be X or Y")
    else:
        board[location[0]][location[1]] = player

move(state,where,xory)
print(f'\nState after move\n{state}')