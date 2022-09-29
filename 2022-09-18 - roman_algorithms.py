#https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        acumulatedNumbers = 0
        reducedNumbers = {
            "M": ["C"],
            "D": ["C"],
            "C": ["X"],
            "L": ["X"],
            "X": ["I"],
            "V": ["I"],
            "I": []
        }
        
        numberValues = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        

        index = len(s) - 1
        while( index >= 0):
            
            romanNumber = s[index]
            
            if index > 0:
                indexAhead = index -1

                romanNumberAhead = s[indexAhead]
                if romanNumberAhead in reducedNumbers[romanNumber]:
                    acumulatedNumbers += numberValues[romanNumber] - numberValues[romanNumberAhead]
                    index -= 2
                    continue
       
    
            acumulatedNumbers += numberValues[romanNumber]
            index -= 1
            
        return acumulatedNumbers
            
            
            
        