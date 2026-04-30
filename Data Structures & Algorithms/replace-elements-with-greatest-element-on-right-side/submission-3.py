class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j] > rmax:
                    rmax = arr[j]
                    arr[i] = arr[j]
            arr[i] = rmax
            rmax = 0
        arr[-1] = -1
        return arr
