class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = math.isqrt(c)
        while a <= b:
            s = a ** 2 + b ** 2
            if s == c:
                return True
            elif s < c:
                a += 1
            else:
                b -= 1
        return False
                
                

            
        

        