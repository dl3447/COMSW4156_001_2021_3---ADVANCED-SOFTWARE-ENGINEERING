import unittest
from Gameboard import Gameboard


class Test_TestGameboard(unittest.TestCase):
    def test_gameboard_init(self):
        gameboard = Gameboard()
        self.assertEqual(gameboard.player1, "")
        self.assertEqual(gameboard.player2, "")
        self.assertEqual(gameboard.game_result, "")
        self.assertEqual(gameboard.current_turn, "p1")
        self.assertEqual(gameboard.remaining_moves, 42)
        self.assertEqual(len(gameboard.board), 6)
        for line in gameboard.board:
            self.assertEqual(len(line), 7)
        for line in gameboard.board:
            for a in line:
                self.assertEqual(a, 0)

    def test_move_p1(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        self.assertEqual(gameboard.board[-1][0], 1)

    def test_move_invalid_column(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        self.assertEqual(gameboard.move(1, 8),
                         (False, 'Invalid column.'))
        self.assertEqual(gameboard.move(1, 0),
                         (False, 'Invalid column.'))

    def test_move_p2(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        gameboard.move(2, 2)
        self.assertEqual(gameboard.board[-1][0], 1)
        self.assertEqual(gameboard.board[-1][1], 2)

    def test_move_p2_stack(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        self.assertEqual(gameboard.board[-1][0], 1)
        self.assertEqual(gameboard.board[-2][0], 2)

    def test_move_p1_not_your_turn(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        self.assertEqual(gameboard.move(1, 1),
                         (False, 'It is not your turn.'))

    def test_move_p2_not_your_turn(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        self.assertEqual(gameboard.move(2, 1),
                         (False, 'It is not your turn.'))

    def test_move_column_full(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        self.assertEqual(gameboard.board[-1][0], 1)
        self.assertEqual(gameboard.board[-2][0], 2)
        self.assertEqual(gameboard.board[-3][0], 1)
        self.assertEqual(gameboard.board[-4][0], 2)
        self.assertEqual(gameboard.board[-5][0], 1)
        self.assertEqual(gameboard.board[-6][0], 2)
        self.assertEqual(gameboard.move(1, 1), (False, 'This column is full'))

    def test_move_game_over(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 2)
        gameboard.move(2, 2)
        gameboard.move(1, 3)
        gameboard.move(2, 3)
        gameboard.move(1, 4)
        self.assertEqual(gameboard.move(2, 3),
                         (False, 'The game is over'))

    def test_move_board_full(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        for _ in range(3):
            for column in [1, 2, 3, 6, 7]:
                gameboard.move(1, column)
                gameboard.move(2, column)
        for _ in range(3):
            gameboard.move(1, 5)
            gameboard.move(2, 4)
            gameboard.move(1, 4)
            gameboard.move(2, 5)
        self.assertEqual(gameboard.move(2, 3),
                         (False, 'The board is full'))

    def test_check_winner_vertial(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
        ]
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p1')
        gameboard.player1 = 2
        gameboard.player2 = 1
        gameboard.game_result = ""
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p2')

    def test_check_winner_diagnal(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 1],
            [0, 2, 2, 2, 1, 1, 1],
        ]
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p1')
        gameboard.player1 = 2
        gameboard.player2 = 1
        gameboard.game_result = ""
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p2')

    def test_check_winner_counter_diagnal(self):
        gameboard = Gameboard()
        gameboard.player1 = 1
        gameboard.player2 = 2
        gameboard.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 1, 2, 2],
            [0, 1, 1, 1, 2, 2, 2],
        ]
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p1')
        gameboard.player1 = 2
        gameboard.player2 = 1
        gameboard.game_result = ""
        gameboard.check_winner()
        self.assertEqual(gameboard.game_result, 'p2')
