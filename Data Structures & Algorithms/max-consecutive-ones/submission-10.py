class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maximum = 0, 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                maximum = max(maximum, count)
                count = 0
        return max(maximum, count)