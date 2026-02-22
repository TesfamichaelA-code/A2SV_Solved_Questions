class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = set(nums)
        count = 0
        for i in long:
            if i - 1 not in long:
                current = i
                streak = 1
                while current + 1 in long:
                    current += 1
                    streak += 1
            
                count = max(count, streak)
        return count
            




        