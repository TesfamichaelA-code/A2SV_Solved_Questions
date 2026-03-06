class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for number in image:
            number.reverse()
            for i in range(len(number)):
                number[i] = 1 - number[i]

            
        return  image


        