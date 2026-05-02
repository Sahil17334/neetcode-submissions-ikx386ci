class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        records = []
        for e in operations:
            if e == '+':
                new_score = records[-1]+records[-2]
                records.append(new_score)
                res += new_score

            elif e == 'D':
                new_score = records[-1] * 2
                records.append(new_score)
                res += new_score

            elif e == 'C':
                res -= records.pop()

            else:
                new_score = int(e)
                records.append(new_score)
                res += new_score
        return res