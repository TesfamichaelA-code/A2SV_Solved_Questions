class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter({0:1})
        ans = 0
        s = 0
        for num in nums:
            s += num
            ans += count[s - k]
            count[s] += 1
        return ans