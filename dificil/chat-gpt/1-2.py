from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')

        for num in nums:
            if num > first_max:
                first_max, second_max, third_max = num, first_max, second_max
            elif first_max > num > second_max:
                second_max, third_max = num, second_max
            elif second_max > num > third_max:
                third_max = num

        return third_max if third_max != float('-inf') else first_max

