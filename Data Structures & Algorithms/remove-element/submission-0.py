class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []
        for element in nums:
            if element != val:
                arr.append(element)

        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)