import unittest
from Gameboard import Gameboard
import db
from contextlib import contextmanager
import sys
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Test_TestDb(unittest.TestCase):
    def test_init_db(self):
        db.clear()
        with captured_output() as (out, err):
            db.init_db()
        out = out.getvalue().strip()
        self.assertEqual(out, 'Database Online, table created')

    def test_init_db_exists(self):
        db.init_db()
        with captured_output() as (out, err):
            db.init_db()
        out = out.getvalue().strip()
        self.assertEqual(out, 'table GAME already exists')

    def test_clear(self):
        db.init_db()
        with captured_output() as (out, err):
            db.clear()
        out = out.getvalue().strip()
        self.assertEqual(out, 'Database Cleared')

    def test_clear_non_exists(self):
        db.clear()
        with captured_output() as (out, err):
            db.clear()
        out = out.getvalue().strip()
        self.assertEqual(out, 'no such table: GAME')

    def test_add_move(self):
        db.clear()
        db.init_db()
        gameboard = Gameboard()
        gameboard.player1 = 'p1'
        gameboard.player2 = 'p2'
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)

    def test_add_move_error(self):
        db.clear()
        gameboard = Gameboard()
        gameboard.player1 = 'p1'
        gameboard.player2 = 'p2'
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        gameboard.move(1, 1)
        gameboard.move(2, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        with captured_output() as (out, err):
            db.add_move(move)
        out = out.getvalue().strip()
        self.assertEqual(out, 'no such table: GAME')

    def test_get_move(self):
        db.clear()
        db.init_db()
        gameboard = Gameboard()
        gameboard.player1 = 'p1'
        gameboard.player2 = 'p2'
        gameboard.move(1, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)
        gameboard.move(2, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)
        gameboard.move(1, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)
        gameboard.move(2, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)
        gameboard.move(1, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)
        gameboard.move(2, 1)
        move = (
            gameboard.current_turn,
            gameboard.board,
            gameboard.game_result,
            gameboard.player1,
            gameboard.player2,
            gameboard.remaining_moves
        )
        db.add_move(move)
        move_in_db = db.getMove()
        self.assertEqual(move, move_in_db)

    def test_get_move_no_move(self):
        db.clear()
        db.init_db()
        gameboard = Gameboard()
        gameboard.player1 = 'p1'
        gameboard.player2 = 'p2'
        move_in_db = db.getMove()
        self.assertEqual(move_in_db, None)

    def test_get_move_error(self):
        db.clear()
        with captured_output() as (out, err):
            db.getMove()
        out = out.getvalue().strip()
        self.assertEqual(out, 'no such table: GAME')
