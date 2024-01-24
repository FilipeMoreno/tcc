class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_attack(i, j):
            for k in range(0,n):
                if board[i][k]=='Q' or board[k][j]=='Q':
                    return True
            for k in range(0,n):
                for l in range(0,n):
                    if (k+l==i+j) or (k-l==i-j):
                        if board[k][l]=='Q':
                            return True
            return False

        def N_queen(n, i, board):
            if i==n:
                res.append([''.join(row) for row in board])
                return
            for j in range(0,n):
                if not is_attack(i, j):
                    board[i][j] = 'Q'
                    N_queen(n, i+1, board)
                    board[i][j] = '.'

        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        N_queen(n, 0, board)
        return res