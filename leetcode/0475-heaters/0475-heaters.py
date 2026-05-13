class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        radius = 0
        
        for house in houses:
            idx = bisect_left(heaters, house)
            
            left_dist = float('inf')
            right_dist = float('inf')
            
            if idx > 0:
                left_dist = house - heaters[idx - 1]
            
            if idx < len(heaters):
                right_dist = heaters[idx] - house
            
            nearest_heater = min(left_dist, right_dist)
            
            radius = max(radius, nearest_heater)
        
        return radius