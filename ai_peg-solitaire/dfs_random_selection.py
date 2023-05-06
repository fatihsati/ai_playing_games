from board import Board
from main import *
import time
import random

# Fatih Satı - 150119625
# Mehmet Selman Baysan - 150120841


def main():
    ALGORITHM = 'DFS Random Selection'
    TIME_LIMIT = 3600
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    frontier = [board]
    start_time = time.time()
    explored_node_count = 0
    max_node_in_memory = 0
    min_left_peg = 32
    explored_node_count = 0
    sub_optimal_solution_node = None
    
    while frontier:
        if len(frontier) > max_node_in_memory:
            max_node_in_memory = len(frontier)
        node = frontier.pop(-1)
        explored_node_count += 1
        
        if time.time() - start_time >= TIME_LIMIT:      # check if time limit is exceeded
            # time limit exceeded, return message
            time_spent = round(time.time() - start_time, 2)    # calculate time spent, round to 2 decimal places
            board_list = get_parents(sub_optimal_solution_node)    # get the board list, solution to inital board
            output_function(ALGORITHM, TIME_LIMIT, 'cutoff', min_left_peg, board_list, time_spent, explored_node_count, max_node_in_memory, 'Time Limit')   # print the output in the required format
            return # print the output and stop executing.
        
        if check_if_board_is_solved(node.board):    # check if the board is solved
            # solution found, return message
            time_spent = round(time.time() - start_time, 2)   # calculate time spent
            board_list = get_parents(node)    # get the board list, solution to inital board
            output_function(ALGORITHM, TIME_LIMIT, 'Optimal', min_left_peg, board_list, time_spent, explored_node_count, max_node_in_memory, 'None')    # print the output in the required format
            return # print the output and stop executing.
        
        # if not solved, check remaining pegs
        left_peg = get_remaining_peg(node.board)    # get the number of remaining pegs
        if left_peg < min_left_peg:    # update the minimum number of remaining pegs
            min_left_peg = left_peg
            sub_optimal_solution_node = node    # save the node for sub optimal solution
        
        # get possible moves and add to frontier
        moves = get_possible_moves(node.board)  # get possible moves
        random.shuffle(moves)       # random selection by shuffling the child list.
        for start, end in moves:
            child = Board(move_peg(node.board, start, end), node, node.depth + 1)   # create a child node
            if child in frontier:   # check if child is already in frontier
                continue
            frontier.append(child)  # add child to frontier
    
    
if __name__ == '__main__':
    main()
    