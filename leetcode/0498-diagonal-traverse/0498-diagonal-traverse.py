class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
    
        m, n = len(mat), len(mat[0])
        result = []

        for s in range(m + n - 1):
            if s % 2 == 0:
                r = min(s, m - 1)
                c = s - r
                while r >= 0 and c < n:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(s, n - 1)
                r = s - c
                while c >= 0 and r < m:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
                    
        return result
            