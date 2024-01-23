from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle the case when the input array is empty
        if not strs:
            return ""

        # Sort the array of strings
        strs.sort()

        # Take the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        # Convert the list of characters back to a string
        return ''.join(common_prefix)