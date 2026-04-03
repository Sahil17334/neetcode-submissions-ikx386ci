class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []

        for element in s:
            if element in mapping:
                if stack and stack[-1] == mapping[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        
        if not stack:
            return True
        return False