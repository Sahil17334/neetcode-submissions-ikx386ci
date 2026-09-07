class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        temp = []
        for n in nums:
            if n != val:
                temp.append(n)
        
        for i in range(len(temp)):
            nums[i] = temp[i]
            k += 1
        
        return k
            