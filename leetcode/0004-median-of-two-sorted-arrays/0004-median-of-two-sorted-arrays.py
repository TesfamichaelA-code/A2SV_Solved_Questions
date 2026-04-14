class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a
        
        m, n = len(a), len(b)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            l1 = a[i - 1] if i > 0 else float('-inf')
            r1 = a[i] if i < m else float('inf')
            
            l2 = b[j - 1] if j > 0 else float('-inf')
            r2 = b[j] if j < n else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            
            if l1 > r2:
                high = i - 1
            else:
                low = i + 1