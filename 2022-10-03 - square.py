import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        lowerLimit = 0        
        upperLimit = x // 2 + 1
        
        if x == 1:
            return 1
        
        while True:
            middle = (lowerLimit + upperLimit) // 2
            
            square = middle * middle
            nextSquare = (middle + 1) * (middle + 1)

            if square <= x < nextSquare:
                return middle
            elif square < x:
                lowerLimit = middle
            else:
                upperLimit = middle
 


class SolutionTwo(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        lowerLimit = 0        
        upperLimit = x // 2 + 1
        
        while lowerLimit <= upperLimit:
            middle = (lowerLimit + upperLimit) // 2
            
            square = middle * middle
            nextSquare = (middle + 1) * (middle + 1)

            if square <= x < nextSquare:
                return middle
            elif square < x:
                lowerLimit = middle
            else:
                upperLimit = middle
  
        # checks which one of the the upper and lower limits is closer to x and still lower than x.
        squareUpper = upperLimit * upperLimit
        root = upperLimit if squareUpper <= x else lowerLimit

        return root
        

class SolutionThree(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        greathestSquare = 0        
        for number in range(x):
            square = number * number
            
            if int(square) <= x:
                greathestSquare = number
            else:
                break
                
        return greathestSquare
number = 8
print(Solution().mySqrt(number))
print(math.sqrt(number))