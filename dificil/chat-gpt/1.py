from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col, n):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check if there is a queen in the left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # Check if there is a queen in the right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False

            return True

        def solve(board, row, n, result):
            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board, row, col, n):
                    board[row][col] = 'Q'
                    solve(board, row + 1, n, result)
                    board[row][col] = '.'

        result = []
        # Initialize an empty chessboard
        chessboard = [['.' for _ in range(n)] for _ in range(n)]

        solve(chessboard, 0, n, result)

        return result

# Example usage:
solution = Solution()
print(solution.solveNQueens(4))
print(solution.solveNQueens(1))
