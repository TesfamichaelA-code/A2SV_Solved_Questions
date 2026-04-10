class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dep = 0
        for i in logs:
            if i == "../":
                dep = max(0, dep - 1)
            elif i == "./":
                continue
            else:
                dep += 1
        return dep