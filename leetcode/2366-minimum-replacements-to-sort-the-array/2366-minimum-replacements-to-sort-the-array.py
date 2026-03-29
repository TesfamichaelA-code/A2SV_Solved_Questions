class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        max_val = nums[-1] 

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= max_val:
                max_val = nums[i]  
                continue

            k = math.ceil(nums[i] / max_val)
            ops += k - 1                       
            max_val = nums[i] // k            

        return ops