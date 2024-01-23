class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store the values of Roman numerals
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the result variable
        result = 0

        # Iterate through the Roman numeral string
        for i in range(len(s)):
            # Check if the current numeral is smaller than the next numeral
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                # Subtract the current value
                result -= roman_values[s[i]]
            else:
                # Add the current value
                result += roman_values[s[i]]

        return result