class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                sign = 1
                num = 0
            elif char == '-':
                result += sign * num
                sign = -1
                num = 0
            elif char == '(':
                stack.append((result, sign))
                result, sign = 0, 1
            elif char == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        result += sign * num
        return result
