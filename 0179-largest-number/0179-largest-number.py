class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = [str(num) for num in nums]
        def compare(a: str, b:str):
            if a + b < b + a:
                return 1
            else:
                return -1
        res.sort(key = cmp_to_key(compare)) 
        if res[0] == "0":
            return "0"

        return "".join(res)
        