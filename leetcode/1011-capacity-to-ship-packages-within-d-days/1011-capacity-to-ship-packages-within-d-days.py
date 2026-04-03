class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            d = 1
            curr = 0
            
            for w in weights:
                if curr + w > capacity:
                    d += 1
                    curr = 0
                curr += w
            
            return d <= days
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid   
            else:
                left = mid + 1  
        
        return left