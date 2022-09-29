#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        
        integer = 0
        sign = 1
        index = 0
        length = len(s)
        
        for runningIndex in range(index, length):
            char = s[runningIndex] 
            if char == " ":
                index += 1
            else:
                break
        
        if index < length and (s[index] == "-" or s[index] == "+"):
            if s[index] == "-":
                sign = -1
            index += 1
        
        
        for runningIndex in range(index, length):
            char = s[runningIndex]
            if char.isnumeric():
                newNumber = int(char)
                integer = integer * 10 + newNumber
            else:
                break
        
        return max(-2**31, min(sign * integer,2**31-1))                
                


# Solution with flags
class SolutionTwo:
    def myAtoi(self, s: str) -> int:
        
        integer = 0
        
        canWhitespaceBeIgnored = True
        canSignBeSet = True
        
        sign = 1
        
        for char in s:  
            if canWhitespaceBeIgnored and char == " ":
                continue
            elif canSignBeSet and (char == "-" or char == "+"):
                if char == "-":
                    sign = -1
                canSignBeSet = False
                canWhitespaceBeIgnored = False
            elif char.isnumeric():
                newNumber = int(char)
                integer = integer * 10 + newNumber
                canSignBeSet = False
                canWhitespaceBeIgnored = False
            else:
                break
        
        
        return max(-2**31, min(sign * integer,2**31-1))                
                