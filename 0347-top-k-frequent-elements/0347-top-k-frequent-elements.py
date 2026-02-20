class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_freq = freq.most_common(k)
        return [num for num, _ in top_freq]

        