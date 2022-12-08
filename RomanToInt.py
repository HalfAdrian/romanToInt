class Solution(object):
    def romanToInt(self, s):
        romandict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        value = 0
        if(len(s) >= 1 & len(s)<=15):
            for i in range(len(s)):
                try:
                    if s[i] in romandict.keys():
                        if s[i] == "I":
                            if s[i+1] == "V" or s[i+1] == "X":
                                value -= 1
                            else:
                                value += 1
                        elif s[i] == "V":
                            value += 5
                        elif s[i] == "X":
                            if s[i+1] == "L" or s[i+1] == "C":
                                value -= 10
                            else:
                                value += 10
                        elif s[i] == "L":
                            value += 50
                        elif s[i] == "C":
                            if s[i+1] == "D" or s[i+1] == "M":
                                value -= 100
                            else:
                                value += 100
                        elif s[i] == "D":
                            value += 500
                        elif s[i] == "M":
                            value += 1000
                        else:
                            value +=0 
                except IndexError:
                    value += romandict[s[i]]
        else:
            return -1
        return value 

object1 = Solution()
print('Enter roman numeral')
romanstr = input().upper()
print('Your roman numera ' +romanstr, ' is ' +str(object1.romanToInt(romanstr)))
                    


                        





