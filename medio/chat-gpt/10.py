from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            if index == len(word):
                return True

            if (
                row < 0
                or col < 0
                or row >= len(board)
                or col >= len(board[0])
                or board[row][col] != word[index]
            ):
                return False

            # Mark the cell as visited
            temp, board[row][col] = board[row][col], "/"

            # Explore in all four directions
            if (
                backtrack(row + 1, col, index + 1)
                or backtrack(row - 1, col, index + 1)
                or backtrack(row, col + 1, index + 1)
                or backtrack(row, col - 1, index + 1)
            ):
                return True

            # Backtrack: restore the cell value
            board[row][col] = temp

            return False

        # Iterate over each cell in the board and start the search
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True

        return False

# Example usage:
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
solution = Solution()
print(solution.exist(board1, word1))  # Output: True
