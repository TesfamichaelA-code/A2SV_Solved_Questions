class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1 = None
        candidate_2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate_1:
                count1 += 1
            elif num == candidate_2:
                count2 += 1
            elif count1 == 0:
                candidate_1 = num
                count1 = 1
            elif count2 == 0:
                candidate_2 = num
                count2 = 1
            else: 
                count1 -= 1
                count2 -= 1
    
            print(candidate_1)
            print(candidate_2)
            print(count1)
            print(count2)
            print()
        arr = []
        n = len(nums) // 3
        if nums.count(candidate_1) > n:
            arr.append(candidate_1)
        if nums.count(candidate_2)  > n:
            arr.append(candidate_2)
        return arr
        

       

        

            



        