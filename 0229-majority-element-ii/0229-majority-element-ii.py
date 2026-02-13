class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums) // 3
        count = Counter(nums)
        for num in count:
            if count[num] > n:
                arr.append(num)
        return arr


            



        