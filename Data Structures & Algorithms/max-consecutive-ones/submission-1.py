class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = count = 0

        for element in nums:
            if element == 1:
                count += 1
            else:
                maximum = max(count, maximum)
                count = 0
        return max(count, maximum)