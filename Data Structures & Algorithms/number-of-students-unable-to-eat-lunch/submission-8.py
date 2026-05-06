class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        cnt = 0
        while q and sandwiches:
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                cnt = 0
            else:
                q.append(q.popleft())
                cnt += 1
            if cnt == len(q):
                break
        return len(q)