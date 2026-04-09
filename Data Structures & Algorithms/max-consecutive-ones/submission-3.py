class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maximum = 0

        for e in nums:
            if e == 1:
                count += 1
                maximum = max(count, maximum)
            elif e == 0:
                count = 0
        return maximum