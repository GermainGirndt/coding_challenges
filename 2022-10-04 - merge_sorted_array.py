#https://leetcode.com/problems/merge-sorted-array/submissions/

#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        self.pointerOneIndex = m - 1
        self.pointerTwoIndex = n - 1
        self.firstArray = nums1
        self.secondArray = nums2

        writeIndex = m + n - 1

        # Pointer two turning to -1 will always determine the end of the algorithm
        # since that means that the second list elements have been completely inserted into the right place
        # in the first list, which is also sorted

        while self.isSecondListDone():
            if self.isFirstListDone() and self.isNextElementFromFirstArrayGreather():
                nums1[writeIndex] = nums1[self.pointerOneIndex]
                self.pointerOneIndex -= 1
            else:
                nums1[writeIndex] = nums2[self.pointerTwoIndex]
                self.pointerTwoIndex -= 1
            
            writeIndex -= 1

    def isFirstListDone(self):
        return self.pointerOneIndex >= 0
    
    def isSecondListDone(self):
        return self.pointerTwoIndex >= 0
    
    def isNextElementFromFirstArrayGreather(self):
        return self.firstArray[self.pointerOneIndex] > self.secondArray[self.pointerTwoIndex]





class SolutionTwo(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        iterationNumber = 0
        maxIterations = m + n
        
        pointerOneIndex = 0
        pointerTwoIndex = 0
        
        firstEmptyIndex = m
        
        # replace 0s with the smallest numbers in place
        # that means:
        # A = [2, 3, 4, 5, 0, 0, 0]
        # B = [1, 2, 5]
        # Result:
        # A = [3, 4, 5, 5, 1, 2, 2] 
        while iterationNumber < maxIterations:
            
            isFirstArrayDone = pointerOneIndex == m
            isSecondArrayDone = pointerTwoIndex == n
            
            useOne = isSecondArrayDone or (not isFirstArrayDone and nums1[pointerOneIndex] <= nums2[pointerTwoIndex])
            correctedIndex = iterationNumber + firstEmptyIndex if iterationNumber + firstEmptyIndex < maxIterations  else iterationNumber + firstEmptyIndex - maxIterations
            
            
            if useOne:
                nums1[correctedIndex] = nums1[pointerOneIndex]
                pointerOneIndex += 1
            else:
                nums1[correctedIndex] = nums2[pointerTwoIndex]
                pointerTwoIndex += 1
            iterationNumber += 1
    

        # correct shifts
        # A = [3, 4, 5, 5, 1, 2, 2] 
        # turns to
        # A = [1, 2, 2, 3, 4, 5, 5]
        numberOfShifts = 0
        while numberOfShifts < firstEmptyIndex:

            firstCorrectedIndex = 0
            firstReplacedValue = nums1[firstCorrectedIndex]

            for index in range(len(nums1) - 1):

                nums1[index] = nums1[index + 1]
            
            nums1[len(nums1) - 1 ] = firstReplacedValue

            numberOfShifts += 1
                



arrayOne = [4, 0, 0, 0, 0, 0]
m = 1
arrayTwo = [1, 2, 3, 5, 6]
n = 5

Solution().merge(arrayOne, m, arrayTwo, n)
print(arrayOne)