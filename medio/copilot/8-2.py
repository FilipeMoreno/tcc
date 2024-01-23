from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            # Add one to the current digit
            digits[i] += 1
            
            # If there is no carry, we can return the updated digits
            if digits[i] < 10:
                return digits
            
            # If there is a carry, set the current digit to 0
            digits[i] = 0
        
        # If we are here, it means there is a carry after iterating through all digits
        # Add a new digit '1' at the beginning of the array
        digits.insert(0, 1)
        
        return digits
