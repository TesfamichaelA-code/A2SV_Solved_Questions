class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        size, end = 0, 0
        result = []
        for i, c in enumerate(s):
            last[c] = i
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                result.append(size)
                size = 0
        return result
        


