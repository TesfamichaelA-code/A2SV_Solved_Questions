class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumulative = 0
        min_cumulative = float('inf')
        for num in nums:
            cumulative += num
            min_cumulative = min(min_cumulative, cumulative)
        return max(1, 1 - min_cumulative)