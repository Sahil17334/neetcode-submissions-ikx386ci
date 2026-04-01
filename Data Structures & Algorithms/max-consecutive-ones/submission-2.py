class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0

        for element in nums:
            if element == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result