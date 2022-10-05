# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 


# The Solution consists of traversing the array from right to left
# In each iteration we're incrementing the number and
# if a carry is generated, repeating the process
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # last index
        index = len(digits) - 1

        # determines if the +1 increment should be executed
        useCarry = True

        while useCarry and index != -1:
            incrementedDigit = digits[index] + 1

            if incrementedDigit < 10:
                digits[index] = incrementedDigit
                useCarry = False
            else:
                digits[index] = 0
                useCarry = True

            # update index for next iteration
            index -= 1

        # if the carry is still true, it means that the number is 9, 99, 999, 9999, etc
        if useCarry:
            # at the index 0, insert a new value 1
            digits.insert(0, 1)
        
        return digits