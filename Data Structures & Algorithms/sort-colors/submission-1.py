class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        
        idx = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[idx] = i
                idx += 1
        return nums
