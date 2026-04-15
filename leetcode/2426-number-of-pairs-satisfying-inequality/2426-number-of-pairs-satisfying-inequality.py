class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)] 
        sor = []
        count = 0
        
        for val in arr:
            count += bisect_right(sor, val + diff)
            insort(sor, val)
        
        return count