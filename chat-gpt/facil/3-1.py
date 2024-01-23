class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the complement of each number
        seen = {}

        for i, num in enumerate(nums):
            # Calculate the complement for the current number
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in seen:
                # If found, return the indices of the two numbers
                return [seen[complement], i]
            
            # If not found, add the current number and its index to the dictionary
            seen[num] = i

        # If no solution is found, return an empty list
        return []
