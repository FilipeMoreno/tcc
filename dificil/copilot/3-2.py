class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the complement of each number and its index
        num_dict = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # Return the indices of the two numbers that add up to the target
                return [num_dict[complement], i]
            
            # If complement is not in the dictionary, add the current number and its index to the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list (this should not happen based on the problem statement)
        return []
