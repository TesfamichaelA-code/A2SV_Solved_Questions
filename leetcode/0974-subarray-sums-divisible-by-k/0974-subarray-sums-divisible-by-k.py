class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         count = {0: 1}
         prefixSum = 0
         result = 0
        
         for num in nums:
             prefixSum += num
             mod = prefixSum % k
            
             if mod < 0:
                 mod += k
            
             if mod in count:
                 result += count[mod]
            
             count[mod] = count.get(mod, 0) + 1
        
         return result