class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Define a mapping for the opening and closing brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        # Iterate through the input string
        for char in s:
            # If the current character is a closing bracket
            if char in bracket_mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the corresponding opening bracket
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # The stack should be empty if all brackets are properly closed
        return not stack