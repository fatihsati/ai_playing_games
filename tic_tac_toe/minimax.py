# an implementation of the minimax algorithm on tic-tac-toe

from game import check_if_game_over, check_if_tie, make_move



def minimax(board, maximizing):
    case = utility(board, 'X')
    if case == 1:   # x is wining
        return 1, None
    if case == -1:  # x is losing
        return -1, None
    if case == 0:   # tie
        return 0, None
    
    
    if maximizing:
        max_eval = -1000
        best_move = None
        posbbile_moves = get_possible_moves(board)
        for row, col in posbbile_moves:
            temp_board = make_move(board, 'X', row, col)
            eval = minimax(temp_board, False)[0]

            if eval > max_eval:
                max_eval = eval
                best_move = (row, col)
                
        return max_eval, best_move
    
    if not maximizing:
        min_eval = 1000
        best_move = None
        
        posbbile_moves = get_possible_moves(board)
        for row, col in posbbile_moves:
            temp_board = make_move(board, 'O', row, col)
            eval = minimax(temp_board, True)[0]

            if eval < min_eval:
                min_eval = eval
                best_move = (row, col)
                
        return min_eval, best_move
   

def get_opponent(plyr):
    """Return the opponent of the player"""
    return 'X' if plyr == 'O' else 'O'

def utility(board, plyr):
    """Return the utility value of the board"""
    opponent = get_opponent(plyr)
    if check_if_game_over(board, plyr):
        return 1
    elif check_if_tie(board):
        return 0
    elif check_if_game_over(board, opponent):
        return -1

def get_possible_moves(board):
    """Return a list of possible moves for the current board"""
    possible_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                possible_moves.append((row+1, col+1)) 
    return possible_moves

