class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        for num in nums:
            actual_sum += num
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - actual_sum

            
            
        