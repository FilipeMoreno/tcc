class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxNumber(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]

        def merge(max1, max2):
            result = []
            i, j = 0, 0
            while i < len(max1) and j < len(max2):
                if max1[i:] > max2[j:]:
                    result.append(max1[i])
                    i += 1
                else:
                    result.append(max2[j])
                    j += 1
            result.extend(max1[i:])
            result.extend(max2[j:])
            return result

        result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            max1 = getMaxNumber(nums1, i)
            max2 = getMaxNumber(nums2, k - i)
            merged = merge(max1, max2)
            result = max(result, merged)

        return result
