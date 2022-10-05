# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        corresponding_opening = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            
            opening_expected = corresponding_opening.get(char)
            
            if opening_expected: # actual is closing
                
                areThereOpeningsLeftToClose = len(stack) != 0 
                if not areThereOpeningsLeftToClose:
                    return False
                
                theWrongOpeningShouldBeClosed = stack.pop() != opening_expected
                if theWrongOpeningShouldBeClosed: # the wrong opening should be closed
                    return False
            else: # is opening
                stack.append(char)

        
        
        return len(stack) == 0 # there are no openings left to close            
        