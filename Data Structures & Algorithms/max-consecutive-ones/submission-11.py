class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maximum = 0, 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            maximum = max(maximum, count)
        return max(maximum, count)