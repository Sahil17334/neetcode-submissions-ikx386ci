class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n

        for i in range(len(arr)):
            rightMax = -1
            for j in range(i + 1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        return ans