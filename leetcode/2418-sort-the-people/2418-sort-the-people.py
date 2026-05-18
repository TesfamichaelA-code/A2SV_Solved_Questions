class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #solved in selection sort
        size = len(heights)
        for i in range(size):
            max_idx = i
            for j in range(i + 1, size):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx]  = names[max_idx], names[i]
        return names 


            

        

        