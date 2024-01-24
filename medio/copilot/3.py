class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x = -x
            is_negative = True

        x = str(x)
        x = x[::-1]
        x = int(x)

        if is_negative:
            x = -x

        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x