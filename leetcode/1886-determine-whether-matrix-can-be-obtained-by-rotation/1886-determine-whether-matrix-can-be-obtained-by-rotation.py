class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(rows) for rows in zip(*mat[::-1])]
            
        return False
"""
       [[0,1],[1,0]]
       [1,0]
       [0,1]
        [0,1]
        [1,0]        
"""
        

        