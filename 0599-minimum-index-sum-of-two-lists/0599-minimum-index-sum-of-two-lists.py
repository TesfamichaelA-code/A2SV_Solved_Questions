class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #find the common strings
        #store there position indexes and sum them
        #if there sum is the leasr then return them
        common = []
        min_sum = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_sum:
                        min_sum = i + j
                        common =[list1[i]]
                    elif i + j == min_sum:
                        common.append(list1[i])
        return common

                
               

                    
        