class Solution:
    def intToRoman(self, num: int) -> str:
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arb = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        i = 0
        s = ""
        while num > 0:
            if (num>=arb[i]):
                s = s+rom[i]
                num -= arb[i]
            else:
                i += 1
        return s