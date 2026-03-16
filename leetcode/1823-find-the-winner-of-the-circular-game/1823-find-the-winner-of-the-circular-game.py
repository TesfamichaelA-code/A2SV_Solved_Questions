class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        value = 0
        for i in range(1, n + 1):
            value = (value + k) % i
        return value + 1



            
            

       

        
        