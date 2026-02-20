class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        check = num % 3
        _sum = num // 3
        if check != 0:
            return []    
        return [_sum - 1, _sum, _sum + 1]
        
        



        