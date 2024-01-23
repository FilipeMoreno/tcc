class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets.values():  # Opening bracket
                stack.append(char)
            elif char in brackets.keys():  # Closing bracket
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                return False  # Invalid character

        return not stack  # If the stack is empty, all brackets are matched.