class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = Counter(nums)
        result = []
        for i in arr:
            if arr[i] > 1:
                result.append(i)
        return result
        
            
        
            
        