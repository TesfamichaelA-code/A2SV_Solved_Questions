class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #receive smallest bills at first
        # receive the next smallest and give back the 5$ on hand
        #if we are out of answers to the given number then return False
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            
            else:
                if bill == 20:
                    if ten > 0 and five > 0:
                        ten -= 1
                        five -= 1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False
        return True
            

                
        
        