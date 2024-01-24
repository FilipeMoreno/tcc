class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Iterate through the array and swap elements to their correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first position where the element is not equal to its index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all elements are in their correct positions, return n + 1
        return n + 1

# Example usage:
solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))  # Output: 3
print(solution.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1
