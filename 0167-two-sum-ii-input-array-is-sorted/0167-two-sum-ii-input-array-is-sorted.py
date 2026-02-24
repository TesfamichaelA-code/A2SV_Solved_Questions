class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        current = 0
        while numbers[i] + numbers[j] != target:
            current = numbers[i] + numbers[j]
            if current < target:    
                i += 1

            else:
                j -= 1
        
        return [i + 1, j + 1]


        