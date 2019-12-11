class TicTacToe:
    def __init__(self, n: int):
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag = [0, 0]
        self.anti = [0, 0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        for group, index in [(self.rows, row), (self.cols, col)]:
            group[index][player - 1] += 1
            if group[index][player - 1] == self.n:
                return player

        if row == col:
            self.diag[player - 1] += 1
        if self.n - row - 1 == col:
            self.anti[player - 1] += 1

        for diag in [self.diag, self.anti]:
            if diag[player - 1] == self.n:
                return player

        return 0
