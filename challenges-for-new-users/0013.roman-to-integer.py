#!/usr/bin/python3

# REF: https://leetcode.com/problems/roman-to-integer/

#
# map strucure ROMAN Symbols TO INT Numbers
#
maprti = {
    "I"  :    1,
    "IV" :    4,
    "V"  :    5,
    "IX" :    9,
    "X"  :   10,
    "XL" :   40,
    "L"  :   50,
    "XC" :   90,
    "C"  :  100,
    "CD" :  400,
    "D"  :  500,
    "CM" :  900,
    "M"  : 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        if (len(s) == 0):
            return 0

        if s[0:2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            return maprti[s[0:2]] + self.romanToInt(s[2:])

        return maprti[s[0:1]] + self.romanToInt(s[1:])

# UNIT TESTING #
pino = Solution()

s = "III"
print(pino.romanToInt(s))

s = "LVIII"
print(pino.romanToInt(s))

s = "MCMXCIV"
print(pino.romanToInt(s))
