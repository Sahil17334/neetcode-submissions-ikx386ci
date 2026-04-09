class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for e in operations:
            if e == '+':
                stack.append(stack[-1] + stack[-2])
            elif e == 'D':
                stack.append(stack[-1] + stack[-1])
            elif e == 'C':
                stack.pop()
            else:
                stack.append(int(e))
            
        sums = 0
        for s in stack:
            sums += s
        return sums