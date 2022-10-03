# https://leetcode.com/problems/remove-element/

#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Time O(n) and Space O(1)
        uniqueNumbersCounter = 0
        for number in nums:
            if number != val:
                nums[uniqueNumbersCounter] = number
                uniqueNumbersCounter += 1
        
        return uniqueNumbersCounter