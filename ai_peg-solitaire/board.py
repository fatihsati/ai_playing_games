
# Fatih Satı - 150119625
# Mehmet Selman Baysan - 150120841


class Board:        
    
    def __init__(self, board, parent=None, depth=0):
        """Class for the node of the tree, which contains current board, parent node and the depth."""
        self.board = board
        self.parent = parent
        self.depth = depth
        
