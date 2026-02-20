class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mode = {}
        for i in nums:
            if i in mode:
                return True
            mode[i] = 1
        return False
            
            
            
             
            
            
            
        