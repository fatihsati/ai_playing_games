from board import Board
from main import *
import time

# Fatih Satı - 150119625
# Mehmet Selman Baysan - 150120841

    
def main():
    ALGORITHM = 'DFS'
    TIME_LIMIT = 3600
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    frontier = [board]
    start_time = time.time()
    explored_node_count = 0
    max_node_in_memory = 0
    min_left_peg = 32
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
        moves = get_possible_moves(node.board)  # get possible moves from the current board
        sorted_boards = heuristic(moves, node.board)    # get the heuristic value for each move
        # get possible moves and add to frontier
        for board in sorted_boards:    # for each possible move
            child = Board(board, node, node.depth + 1)   # create a child node with the move
            if child in frontier:   # if the child is already in frontier, skip
                continue
            frontier.append(child)  # add the child to frontier
        
        # continue the loop until solution is find or time limit is exceeded.
    
if __name__ == '__main__':
    main()
    