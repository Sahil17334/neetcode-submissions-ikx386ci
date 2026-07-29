class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def helper(i, total):
            if i == len(nums) or total >= target:
                if total == target:
                    res.append(subset[:])
                return
            
            subset.append(nums[i])
            total += nums[i]
            helper(i, total)

            subset.pop()
            total -= nums[i]
            helper(i+1, total)
        helper(0, 0)
        return res