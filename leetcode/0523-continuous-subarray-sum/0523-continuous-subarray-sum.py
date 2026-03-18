class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            j = prefix % k
            
            if j in remainder:
                if i - remainder[j] > 1:
                    return True
            else:
                remainder[j] = i
        return False