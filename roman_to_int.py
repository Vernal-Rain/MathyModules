'''Roman numeral to integer, works for 1<=i<=3999'''
#Elaine Lee
#1/24/20

class Solution:
    def romanToInt(self, s: str) -> int:
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i in range(len(s)-1):
            num += (1 if a[s[i]] >= a[s[i+1]] else -1) * a[s[i]]
        return num + a[s[-1]]
        
        

        
