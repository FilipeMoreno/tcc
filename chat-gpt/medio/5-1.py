class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store the values of Roman numerals
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}

        result = 0
        prev_value = 0

        # Iterate through the string from right to left
        for char in reversed(s):
            current_value = roman_values[char]

            # If the current value is less than the previous one, subtract it
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result