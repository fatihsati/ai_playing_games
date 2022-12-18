import game
import unittest




class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = game.initialize_board()
        self.X_wins = [['X', 'X', 'X'],
                         ['O', 'O', None],
                         [None, None, None]]
        
        self.O_wins = [['X', 'O', 'X'],
                          ['O', 'O', 'X'],
                          ['X', 'O', None]]
        
        self.tie = [['X', 'O', 'X'],
                    ['O', 'O', 'X'],
                    ['X', 'X', 'O']]
    
    def test_make_move(self):
        board = game.make_move(self.board, 'X', 0, 0)
        self.assertEqual(board[0][0], 'X')
        board = game.make_move(board, 'O', 0, 1)
        self.assertEqual(board[0][1], 'O')
    
    def test_check_if_game_over(self):
        self.assertTrue(game.check_if_game_over(self.X_wins, 'X'))  # exptected True
        self.assertFalse(game.check_if_game_over(self.X_wins, 'O'))  # expected False
        self.assertTrue(game.check_if_game_over(self.O_wins, 'O'))  # expected True
        self.assertFalse(game.check_if_game_over(self.tie, 'X')) # expected False
        self.assertFalse(game.check_if_game_over(self.tie, 'O')) # expected False
    
    def check_if_tie(self):
        self.assertTrue(game.check_if_tie(self.tie))
    
    

if __name__ == '__main__':
    unittest.main()