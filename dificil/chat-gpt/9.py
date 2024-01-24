class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D array to store the intermediate results of matching
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Fill the first row for patterns with '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Dynamic programming to fill the rest of the table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)

        return dp[len(s)][len(p)]

# Example usage:
solution = Solution()
print(solution.isMatch("aa", "a"))      # Output: False
print(solution.isMatch("aa", "a*"))     # Output: True
print(solution.isMatch("ab", ".*"))     # Output: True
