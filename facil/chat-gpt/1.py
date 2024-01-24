from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize three variables to store the top three maximum values
        first_max = second_max = third_max = float('-inf')

        # Iterate through the array to find distinct maximum values
        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max < num < first_max:
                third_max = second_max
                second_max = num
            elif third_max < num < second_max:
                third_max = num

        # Check if the third maximum exists, otherwise return the overall maximum
        return third_max if third_max != float('-inf') else first_max