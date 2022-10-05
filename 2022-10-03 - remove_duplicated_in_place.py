#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Time O(n) and Space O(1)
# The trick is to make use of the sorted property
# We don't need a hashMap, since for every compared number, we can just check which was the last one seen.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uniqueNumbersCounter = 0
        for number in nums:
            if not self.wasNumberSeen(nums, uniqueNumbersCounter, number):
                nums[uniqueNumbersCounter] = number
                uniqueNumbersCounter += 1
        
        return uniqueNumbersCounter

    def wasNumberSeen(self, nums, uniqueNumbersCounter, number):

        lastUniqueNumberIndex = uniqueNumbersCounter - 1

        # prevents unwanted behaviour when uniqueNumbersCounter is 0 and we try to access nums[- 1]
        if lastUniqueNumberIndex == -1:
            return False
        
        # Since the array is sorted, we can assume that if the number is the same as the last unique number, it's a duplicate
        return nums[lastUniqueNumberIndex] == number




# Time O(n) and Space O(n)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbersSeen = {}
        uniqueCount = 0
        for number in nums:
            if not numbersSeen.get(number):
                numbersSeen[number] = True
                nums[uniqueCount] = number
                uniqueCount += 1
        
        return uniqueCount

