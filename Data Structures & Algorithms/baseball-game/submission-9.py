class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for element in operations:
            if element == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif element == 'D':
                res += stack[-1] * 2
                stack.append(2*stack[-1])
            elif element == 'C':
                res -= stack.pop()
            else:
                stack.append(int(element))
                res += int(element)
        return res