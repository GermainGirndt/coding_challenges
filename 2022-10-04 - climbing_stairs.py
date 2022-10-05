#Runtime: 19 ms, faster than 82.90% of Python online submissions for Climbing Stairs.
#Memory Usage: 13.2 MB, less than 97.05% of Python online submissions for Climbing Stairs.

# The trick is to see that the problem can be decomposed in smaller ones, for which we already know the solution
#
# For instance: if we have 3 steps, at the begining we have just 2 approaches WHICH CAN'T VARY
# 1 - starting with a single step, and then we have 2 more steps left (and we know the base case for 2 is 2)
# 2 - starting with a double step, and then we have 1 more step left (and we know the base case for 1 is 1)
# that means, for 3 levels: 1 + 2 = 3 posibilities
#
# the same way, for 4 steps:
# 1 - single step at start => 3 steps left (base case is 3, as we just calculated)
# 2 - double step at start => 2 steps left (base case is 2, as known)
# that means, for 4 levels: 3 + 2 = 5 possibilities
#
class Solution(object):
    
    def __init__(self):
        # base case
         self.levelsToSteps = {0 : 0, 1 : 1, 2 : 2}
        
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        levels = n

        stepsNumber = self.levelsToSteps.get(levels)
        if stepsNumber is not None:
            return stepsNumber
        
        # else, calculate it:
        stepsNumber = self.climbStairs(levels - 1) + self.climbStairs(levels - 2)
        
        # memoizing the step number for future references
        self.levelsToSteps[levels] = stepsNumber

        return stepsNumber
    

for i in range(501):
    steps = Solution().climbStairs(i)
    print(f"Levels: {i} - Steps: {steps}")