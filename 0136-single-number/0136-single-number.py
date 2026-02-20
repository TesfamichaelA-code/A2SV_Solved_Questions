class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for i in frequency:
            if frequency[i] == 1:
                return i
        