class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 1
        i = 0
        ans = 0
        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                ans += 1
                x *= 2
        return ans

