class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        e = lambda p: p[0]**2 + p[1]**2

        def partition(l, r):
            pivotIndex = r
            pivotDistance = e(points[pivotIndex])
            i = l
            for j in range(l, r):
                if e(points[j]) <= pivotDistance:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i
        
        L, R = 0, len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot+1
            else:
                R = pivot -1
        return points[:k]