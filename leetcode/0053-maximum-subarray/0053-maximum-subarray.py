class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        maximum = float('-inf')
        for i in range(n):
            sum += nums[i]
            if sum > maximum:
                maximum = sum
            if sum < 0:
                sum = 0
        return maximum



            


        