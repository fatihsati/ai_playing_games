# crerate the board
# check if the game is over (win, tie, or lose)
# display the board

# game is played on a 3x3 board from the text command line
# each player is assigned a marker (X or O)

import random_play
import minimax

def initialize_board():
    # 3x3 board, empty cells are represented by None
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    return board

def check_if_game_over(board, plyr):
    # plyr is X or O
    
    # check rows
    for row in board:
        if row == [plyr, plyr, plyr]:
            return True
    
    # check columns
    for column in range(3):
        if board[0][column] == plyr and board[1][column] == plyr and board[2][column] == plyr:
            return True
    
    # check diagonals
    if board[0][0] == plyr and board[1][1] == plyr and board[2][2] == plyr:
        return True
    elif board[0][2] == plyr and board[1][1] == plyr and board[2][0] == plyr:
        return True
    
    return False


def check_if_tie(board):
    # check if the board is full
    for row in board:
        if None in row:
            return False
    return True

def make_move(board, plyr, row, col):
    temp_board = [row[:] for row in board]
    # add a move to the board
    temp_board[row-1][col-1] = plyr
    return temp_board

    
def display_board(board):
    print()
    print('  1 2 3')
    for row in range(len(board)):
        print(row+1, end=' ')
        for cell in board[row]:
            if cell == None:
                print(' ', end=' ')
            else:
                print(cell, end=' ')
        print()
        
def change_turn(turn):
    if turn == 'X':
        return 'O'
    return 'X'

def main():
    # initialize the board
    board = initialize_board()

    turn = 'X'
    ai = minimax.get_opponent(input("Select your marker (X or O): "))
    
    ai_max = True if ai == 'X' else False
    while True: 
        print(f"Turn: {turn}")
        if turn == ai:
            # input_move = random_play.return_random_move(board) # random play
            utilit, input_move = minimax.minimax(board, ai_max)   # minimax algorithm
            print('\n', utilit, input_move)
        else:
            input_move = input(f"Enter your move for {turn}(example: 1 3): ")
            input_move = (int(input_move[0]), int(input_move[2]))
        
        board = make_move(board, turn, input_move[0], input_move[1])
        
        if check_if_game_over(board, turn):
            display_board(board)
            print(f"{turn} wins!")
            break
        if check_if_tie(board):
            display_board(board)
            print('Tie!')
            break
        
        turn = change_turn(turn)
        display_board(board)
        
        
if __name__ == '__main__':
    main()
