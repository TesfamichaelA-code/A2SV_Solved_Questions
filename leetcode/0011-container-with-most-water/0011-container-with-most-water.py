class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        find the two numbers on the starting point and end
        check if they are bigger numbers

        """
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            width = end - start
            current_area = min(height[start], height[end]) * width
            if current_area > max_area:
                max_area = current_area
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area
            
       