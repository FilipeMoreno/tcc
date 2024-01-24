class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        if dividend == 0:
            return 0

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert both dividend and divisor to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize quotient
        quotient = 0

        # Perform binary division
        while dividend >= divisor:
            temp_divisor, temp_quotient = divisor, 1

            # Double the divisor and quotient until it exceeds the dividend
            while dividend >= temp_divisor:
                dividend -= temp_divisor
                quotient += temp_quotient

                temp_divisor <<= 1
                temp_quotient <<= 1

        # Apply sign to the result
        result = sign * quotient

        # Check for overflow
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result

# Example usage:
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
