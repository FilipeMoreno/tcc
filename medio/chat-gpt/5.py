from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Find the first pair (i, i+1) such that nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the rightmost element nums[j] such that nums[j] > nums[i]
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray nums[i+1:]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
