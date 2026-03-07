class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
         res = []
         r, c = rStart, cStart

         directions = [(0,1),(1,0),(0,-1),(-1,0)]  
         steps = 1
         d = 0

         res.append([r,c])

         while len(res) < rows * cols:
             for _ in range(2):
                 dr, dc = directions[d % 4]
                 for _ in range(steps):
                     r += dr
                     c += dc
                     if 0 <= r < rows and 0 <= c < cols:
                         res.append([r,c])
                 d += 1
             steps += 1

         return res