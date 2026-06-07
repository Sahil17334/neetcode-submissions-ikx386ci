class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1
        
        i = 0
        for n in range(len(count)):
            for _ in range(count[n]):
                nums[i] = n
                i += 1
        
        return nums
        