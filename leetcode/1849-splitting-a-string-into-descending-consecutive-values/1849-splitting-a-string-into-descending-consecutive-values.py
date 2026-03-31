class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(index, prev):
            if index == n:
                return True
            
            curr = 0
            for i in range(index, n):
                curr = curr * 10 + int(s[i])
                
                if curr == prev - 1:
                    if dfs(i + 1, curr):
                        return True
                
                if curr >= prev:
                    break
            
            return False

        for i in range(1, n):
            first = int(s[:i])
            if dfs(i, first):
                return True

        return False