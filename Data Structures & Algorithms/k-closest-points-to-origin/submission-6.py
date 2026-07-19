class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euc = lambda x: x[0]**2 + x[1]**2
        
        def partition(l, r):
            pivotIdx = r
            pivotDist = euc(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euc(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i
        
        L, R = 0, len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L += 1
            else:
                R -= 1
        return points[:k]