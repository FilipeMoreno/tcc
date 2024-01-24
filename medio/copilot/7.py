class Solution(object):
    def sortColors(self, nums):
      zeroPointer, umPointer, doisPointer = 0, 0, len(nums) - 1

      while umPointer <= doisPointer:
          if nums[umPointer] == 0:
              nums[zeroPointer], nums[umPointer] = nums[umPointer], nums[zeroPointer]
              zeroPointer += 1
              umPointer += 1
          elif nums[umPointer] == 1:
              umPointer += 1
          else:
              nums[umPointer], nums[doisPointer] = nums[doisPointer], nums[umPointer]
              doisPointer -= 1
        