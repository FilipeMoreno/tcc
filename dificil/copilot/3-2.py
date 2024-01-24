class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1

        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                stack.append(num * sign)
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(sign)
                sign = 1
            elif c == ')':
                stack.append(num * sign)
                num = 0
                total = 0
                while stack and isinstance(stack[-1], int):
                    total += stack.pop()
                if stack:
                    sign = stack.pop()
                    stack.append(total * sign)
                    num = 0

        stack.append(num * sign)
        return sum(stack)