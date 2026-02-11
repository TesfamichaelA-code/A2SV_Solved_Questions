class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in result:
                return result[ans],i 
            result[num] = i


        


        