class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for element in operations:
            if element == '+':
                stack.append(stack[-1] + stack[-2])
            elif element == 'D':
                stack.append(2*stack[-1])
            elif element == 'C':
                stack.pop()
            else:
                stack.append(int(element))
        return sum(stack)