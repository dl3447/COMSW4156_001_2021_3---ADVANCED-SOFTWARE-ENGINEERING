

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42

    def move(self, player, column):
        if self.remaining_moves == 0:
            return (False, 'The board is full')
        if self.game_result != "":
            return (False, 'The game is over')
        column -= 1
        if str(player) not in self.current_turn:
            return (False, 'It is not your turn.')
        if column < 0 or column >= len(self.board[0]):
            return (False, 'Invalid column.')
        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][column] == 0:
                self.board[i][column] = self.player1 \
                    if player == 1 else self.player2
                self.current_turn = 'p2' if self.current_turn == 'p1' else 'p1'
                self.check_winner()
                self.remaining_moves -= 1
                return (True, '')
        # if full, return False
        return (False, 'This column is full')

    def check_winner(self):
        if self.game_result != "":
            return
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    continue
                if all(i + k < len(self.board)
                       and j + k < len(self.board[i])
                       and self.board[i + k][j + k] == self.board[i][j]
                       for k in range(4)):
                    self.game_result = 'p1' \
                        if self.board[i][j] == self.player1 else 'p2'
                    return
                if all(i + k < len(self.board)
                       and j - k >= 0
                       and self.board[i + k][j - k] == self.board[i][j]
                       for k in range(4)):
                    self.game_result = 'p1' \
                        if self.board[i][j] == self.player1 else 'p2'
                    return
                if all(j + k < len(self.board[i])
                       and self.board[i][j + k] == self.board[i][j]
                       for k in range(4)):
                    self.game_result = 'p1' \
                        if self.board[i][j] == self.player1 else 'p2'
                    return
                if all(i + k < len(self.board)
                       and self.board[i + k][j] == self.board[i][j]
                       for k in range(4)):
                    self.game_result = 'p1' \
                        if self.board[i][j] == self.player1 else 'p2'
                    return


'''
Add Helper functions as needed to handle moves and update board and turns
'''
