class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a dictionary to store character counts
        char_count = {}

        # Count characters in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Count characters in string t
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1

        # Find the character with a count of -1 (added in t)
        for char, count in char_count.items():
            if count == -1:
                return char
