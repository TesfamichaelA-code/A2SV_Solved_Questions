class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        
        dominant_element = -1
        total_dominant_count = 0
        
        for x, count in counts.items():
            if count * 2 > n:
                dominant_element = x
                total_dominant_count = count
                break
    
        left_dominant_count = 0
        for i in range(n - 1):
            if nums[i] == dominant_element:
                left_dominant_count += 1

            left_len = i + 1
            right_len = n - left_len

            right_dominant_count = total_dominant_count - left_dominant_count
        
            if (left_dominant_count * 2 > left_len) and (right_dominant_count * 2 > right_len):
                return i
                
        return -1
        