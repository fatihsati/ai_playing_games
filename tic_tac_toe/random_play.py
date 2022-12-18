import random

"""Plays the game by randomly selecting a move from the list of possible moves"""

def get_possible_moves(board):
    """Return a list of possible moves for the current board"""
    possible_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                possible_moves.append(f"{row+1},{col+1}") 
    return possible_moves

def return_random_move(board):
    """Return a random move from the list of possible moves"""
    possible_moves = get_possible_moves(board)
    return random.choice(possible_moves)
    