class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums)
        for i in num:
            if num[i] > 1:
                return True
        return False

            
            
            
             
            
            
            
        