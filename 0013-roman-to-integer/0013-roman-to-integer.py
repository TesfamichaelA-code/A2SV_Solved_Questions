class Solution:
    def romanToInt(self, s: str) -> int:
        roman = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
            ]
        result = 0
        for symbol,value in roman:
            while s.startswith(symbol):
                result += value
                s = s[len(symbol):] 
        return result


        