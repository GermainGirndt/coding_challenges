# https://leetcode.com/problems/container-with-most-water/

# We don't need to compare every container with each other,
# it's more worth it to use a greedy algorithm to should which container will be compaired in the next iteration
#  5 200 1 4
# we just need to compare 5 and 4, 5 and 1 and 5 and5
# in that way, we spare comparing 5 and 1, 5 and 4, 1 and 4

#The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
#All other containers are less wide and thus would need a higher water level in order to hold more water.
#The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:       
        maxWaterAmount = 0
        
        if len(height) == 1 or len(height) == 0:
            return 0
        
        
        numberOfContainers = len(height)
        
        pointerOne = 0
        pointerTwo = numberOfContainers -1
        
        while pointerOne < pointerTwo:
            
            containerOne = height[pointerOne]
            containerTwo = height[pointerTwo]
            lowest = min(containerOne, containerTwo)
            distance = pointerTwo - pointerOne
            waterAmount = lowest * distance

            
            if waterAmount > maxWaterAmount:
                maxWaterAmount = waterAmount 
            
            if containerOne > containerTwo:
                pointerTwo -= 1
            else:
                pointerOne += 1
        
        return maxWaterAmount


print(Solution().maxArea([5, 200, 1, 4]))
        

# How to limite the number of iterations in the container?
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxWaterAmount = 0
        
        if len(height) == 1 or len(height) == 0:
            return 0
        
        numberOfContainers = len(height)
        for pointerOne in range(numberOfContainers):
            for pointerTwo in range(pointerOne + 1, numberOfContainers):
                
                containerOne = height[pointerOne]
                containerTwo = height[pointerTwo]
                lowest = min(containerOne, containerTwo)
                distance = pointerTwo - pointerOne
                waterAmount = lowest * distance
                
                if waterAmount > maxWaterAmount:
                    maxWaterAmount = waterAmount 
            
        
        return maxWaterAmount
            
        