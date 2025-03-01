import sqlite3
from sqlite3 import Error

'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move):  # will take in a tuple
    current_turn, board, winner, player1, player2, remaining_moves = move
    try:
        conn = sqlite3.connect('sqlite_db')
        expression = f"""
        INSERT INTO GAME VALUES
        ('{current_turn}',
        "{board}",
        '{winner}',
        '{player1}',
        '{player2}',
        '{remaining_moves}')
        """
        conn.execute(expression)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails
    try:
        conn = sqlite3.connect('sqlite_db')
        move = conn.execute("SELECT * FROM GAME")
        move = move.fetchall()
        if not move:
            return None
        move = move[-1]
        current_turn, board, winner, player1, player2, remaining_moves = move
        board = eval(board)
        conn.commit()
        conn.close()
        return (current_turn, board, winner, player1, player2, remaining_moves)
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
    return None


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
