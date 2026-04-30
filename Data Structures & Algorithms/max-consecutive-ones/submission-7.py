class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = res = 0
        for element in nums:
            if element == 0:
                cnt = 0
            else:
                cnt += 1
                res = max(cnt, res)
        return res
            
