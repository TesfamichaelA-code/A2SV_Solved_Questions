class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        BIT = [0] * (max_val + 2)

        def update(i):
            while i < len(BIT):
                BIT[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s

        cost = 0
        
        for i, x in enumerate(instructions):
            less = query(x - 1)
            greater = i - query(x)
            cost += min(less, greater)
            cost %= MOD
            
            update(x)
        
        return cost