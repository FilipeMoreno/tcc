from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate through the characters of the first string
        for i, char in enumerate(strs[0]):
            # Check if the character is present in the same position in all other strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    # If not, return the common prefix found so far
                    return strs[0][:i]

        # If all characters match, return the entire first string as the common prefix
        return strs[0]
