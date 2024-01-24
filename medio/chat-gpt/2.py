class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character in the string
        last_index = {}
        # Start and end pointers of the sliding window
        start = 0
        end = 0
        # Maximum length of the substring without repeating characters
        max_length = 0

        while end < len(s):
            # If the character is not in the current substring or its last occurrence is before the start pointer
            if s[end] not in last_index or last_index[s[end]] < start:
                # Update the last index of the character
                last_index[s[end]] = end
                # Update the length of the current substring
                current_length = end - start + 1
                # Update the maximum length if needed
                max_length = max(max_length, current_length)
                # Move the end pointer to the right
                end += 1
            else:
                # Move the start pointer to the right of the last occurrence of the repeating character
                start = last_index[s[end]] + 1

        return max_length
