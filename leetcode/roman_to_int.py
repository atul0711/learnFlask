class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dict_roman = {"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num += dict_roman[s[0]]
        for i in range(1, len(s)):
            # print("num", num)
            if s[i] in ['V', 'X'] and s[i-1] == 'I':
                number = dict_roman[s[i]]-1
                num -= 1
            elif s[i] in ['L', 'C'] and s[i-1] == 'X':
                number = dict_roman[s[i]]-10
                num -= 10
            elif s[i] in ['D', 'M'] and s[i-1] == 'C':
                number = dict_roman[s[i]]-100
                num -= 100
            else:
                number = dict_roman[s[i]]
            num += number
        return num


obj = Solution()
print(obj.romanToInt("MCMXCIV"))