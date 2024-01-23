class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
