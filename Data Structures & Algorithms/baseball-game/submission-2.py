class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        
        for i in range(len(operations)):
            if operations[i] == '+':
                records.append(int(records[-1])+int(records[-2]))
            elif operations[i] == 'D':
                records.append(int(records[-1]*2))
            elif operations[i] == 'C':
                records.pop()
            else:
                records.append(int(operations[i]))
        
        s = 0
        for e in records:
            s += e
        return s