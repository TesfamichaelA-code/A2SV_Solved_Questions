class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(zip(s,indices))
        arr.sort(key=lambda x: x[1])
        return "" .join(char for char, _ in arr)
    
            

        