
# Fatih Satı - 150119625
# Mehmet Selman Baysan - 150120841

# Main operations of the program.
# Creating board, calculating possible moves, moving pegs, checking if board is solved and printing the output.

def print_boards(boards):
    """print the boards in the list in reverse order to get the correct order, from initial board to solution board"""
    for board in reversed(boards): # since boards are stored in reverse order, we need to reverse the list
        for row in board:   
            for each in row:
                if each == -1:      # if the value is -1, print a space instead since -1 is used to represent out of the board.
                    print(' ', end=' ')
                else:
                    print(each, end=' ')  
            print() # print a new line after each row
        print() # print a blank line between boards to make it easier to read

def output_function(method, time_limit, solution_type, remaining_peg, boards, time_spent, explored_node_count, max_number_of_nodes_in_memory, failure_type):
    # board states
    print_boards(boards)
    print(f'Method: {method} - Time limit: {time_limit} seconds')
    if solution_type == 'cutoff':
        print(f'Sub-optimal solution found with {remaining_peg} remaining pegs')
        print(f'No Optimal solution found - {failure_type}')
    else:
        print(f'Optimum solution found.')
    
    print(f'Time spent: {time_spent}')
    print(f'Explored node count: {explored_node_count}')
    print(f'Max number of nodes in memory: {max_number_of_nodes_in_memory}')

def get_parents(node):
    if node.parent is None:
        return [node.board]
    return [node.board] + get_parents(node.parent)

def get_remaining_peg(board):
    return sum(x.count(1) for x in board)

def create_peg_solitaire_board():
    board = [] # create an empty list
    for row in range(7): # iterate through the rows
        board.append([]) # add an empty list to the board
        for col in range(7): # iterate through the columns
            if row in [0,1,5,6] and col in [0,1,5,6]: # if the position is out of the board, add -1 to the board
                board[row].append(-1) 
            elif (row == 3 and col == 3): # if the position is in the middle of the board, add 0 to the board
                board[row].append(0) 
            else: # if the position is in the board, add 1 to the board
                board[row].append(1)  
    return board # return the board

def check_if_board_is_solved(board):
    """Return True if there are only 1 piece left on the board, else return False"""
    peg_number = sum(x.count(1) for x in board) # count the number of pegs in the board
    if peg_number == 1 and board[3][3] == 1: # if there is only 1 peg left and it is in the middle of the board, return True
        return True
    return False # else return False

def move_peg(board, start, end):
    new_board = list(map(list, board)) # create a copy of the board
    if (start[0] == end[0] and abs(start[1] - end[1]) == 2) or (start[1] == end[1] and abs(start[0] - end[0]) == 2): # check if the move is valid
        if new_board[start[0]][start[1]] == 1 and new_board[end[0]][end[1]] == 0: # check if the start and end positions are valid
            if start[0] == end[0]: # if the move is horizontal
                mid = (start[0], (start[1] + end[1]) // 2) # calculate the middle position
            else: # if the move is vertical
                mid = ((start[0] + end[0]) // 2, start[1]) # calculate the middle position
            if new_board[mid[0]][mid[1]] == 1: # check if the middle position is valid
                new_board[start[0]][start[1]] = 0 # move the peg
                new_board[mid[0]][mid[1]] = 0 # remove the peg that was jumped over
                new_board[end[0]][end[1]] = 1 # place the peg in the new position
                return new_board # return the new board
    return False # if the move is not valid, return False

def return_sorted_moves_according_to_removal_peg(moves, reverse=True): # return the removed pegs in the moves
    moves_with_removed_pegs = [] # list to store the moves with removed pegs
    for move in moves: # iterate through the moves
        if move[0][0] == move[1][0]: # if the move is horizontal
            if move[0][1] < move[1][1]: # if the move is right
                moves_with_removed_pegs.append((move, (move[0][0], move[0][1] + 1))) # add the move and the removed peg to the list
            else: # if the move is left
                moves_with_removed_pegs.append((move, (move[0][0], move[0][1] - 1))) # add the move and the removed peg to the list
        else: # if the move is vertical
            if move[0][0] < move[1][0]: # if the move is down
                moves_with_removed_pegs.append((move, (move[0][0] + 1, move[0][1]))) # add the move and the removed peg to the list
            else: # if the move is up
                moves_with_removed_pegs.append((move, (move[0][0] - 1, move[0][1]))) # add the move and the removed peg to the list
    
    moves_with_removed_pegs.sort(key=lambda x: x[1], reverse=reverse) # sort the list by the index of removed peg
    moves_with_removed_pegs = [i[0] for i in moves_with_removed_pegs] # get only moves from the list
    return moves_with_removed_pegs

def get_possible_moves(board):
    moves = [] # list to store the possible moves
    for row in range(7): # iterate through the board
        for col in range(7): # iterate through the board
            if board[row][col] == 1: # if the position is a peg
                if row > 1 and board[row - 1][col] == 1 and board[row - 2][col] == 0: # check if the move is valid
                    moves.append(((row, col), (row - 2, col))) # if it is, add it to the list
                if row < 5 and board[row + 1][col] == 1 and board[row + 2][col] == 0: # check if the move is valid
                    moves.append(((row, col), (row + 2, col))) # if it is, add it to the list
                if col > 1 and board[row][col - 1] == 1 and board[row][col - 2] == 0: # check if the move is valid
                    moves.append(((row, col), (row, col - 2))) # if it is, add it to the list
                if col < 5 and board[row][col + 1] == 1 and board[row][col + 2] == 0: # check if the move is valid
                    moves.append(((row, col), (row, col + 2))) # if it is, add it to the list

    return moves # return the list of possible moves

def heuristic(moves, board):
    boards = [] # list to store boards after the moves
    for move in moves:
        new_board = move_peg(board, move[0], move[1])
        if new_board:
            heuristic_value = average_manhattan_distance(new_board)
            boards.append((new_board, heuristic_value))
    boards.sort(key=lambda x: x[1], reverse=True) # sort the list by the heuristic value
    boards = [i[0] for i in boards] # get only boards from the list
    return boards

def average_manhattan_distance(board):
    """Return the manhattan distance of the board"""
    peg_count = 0
    distance = 0 # initialize the distance
    for row in range(7): # iterate through the board
        for col in range(7): # iterate through the board
            if board[row][col] == 1: # if the position is a peg
                peg_count += 1 # add 1 to the peg count
                distance += abs(row - 3) + abs(col - 3) # add the distance to the middle of the board
    return distance/peg_count # return the distance
