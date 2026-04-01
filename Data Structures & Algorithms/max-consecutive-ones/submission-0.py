class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                count += 1
            if maximum < count:
                maximum = count
        return maximum