class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = list(zip(heights, names))
        pair.sort(reverse=True)
        return [name for height, name in pair]

        

        