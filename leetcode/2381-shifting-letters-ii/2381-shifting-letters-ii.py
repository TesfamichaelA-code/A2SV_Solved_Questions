class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * n
        for shift in shifts:
            if shift[2] == 1:
                diff[shift[0]] += 1
                if shift[1] + 1 < n:
                    diff[shift[1] + 1] -= 1
            else:
                diff[shift[0]] -= 1
                if shift[1] + 1 < n:
                    diff[shift[1] + 1] += 1
        res = list(s)
        nums = 0
        for i in range(n):
            nums = (nums + diff[i]) % 26
            if nums < 0:
                nums += 26
            ch = chr((ord(s[i]) - ord("a") + nums) % 26 + ord ("a"))
            res[i] = ch 
        return "".join(res)  
                    

