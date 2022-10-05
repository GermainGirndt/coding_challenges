# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



### Solution based on recursivity
#### e.g. if a's median is bigger than b's, a's second half doesn't include k

class Solution:
    def findMedianSortedArrays(self, A, B):
        totalLength = len(A) + len(B)
        if totalLength % 2 == 1:
            return self.kth(A, B, totalLength // 2)
        else:
            medianLeft = self.kth(A, B, totalLength // 2 - 1)
            medianRight = self.kth(A, B, totalLength // 2)
            return ( medianLeft + medianRight) / 2
        
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        iA, iB = len(a) // 2 , len(b) // 2
        ma, mb = a[iA], b[iB]
        
        # when k is bigger than the sum of a and b's median indices 
        if iA + iB < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[iB + 1:], k - iB - 1)
            else:
                return self.kth(a[iA + 1:], b, k - iA - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:iA], b, k)
            else:
                return self.kth(a, b[:iB], k)




### First naive solution
class SolutionTwo:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums_merged = []
        
        nums1_index = 0
        nums2_index = 0
        for i in range(len(nums1) + len(nums2)):
            
            is_nums1_traversed = nums1_index >= len(nums1)
            is_nums2_traversed = nums2_index >= len(nums2)
            
            if not is_nums1_traversed and not is_nums2_traversed:
                
                num1 = nums1[nums1_index]
                num2 = nums2[nums2_index]
                
                if num1 <= num2:
                    nums_merged.append(num1)
                    nums1_index += 1
                else:
                    nums_merged.append(num2)
                    nums2_index += 1
            
            elif not is_nums1_traversed and is_nums2_traversed:
                    num1 = nums1[nums1_index]
                    nums_merged.append(num1)
                    nums1_index += 1
            
            elif is_nums1_traversed and not is_nums2_traversed:
                    num2 = nums2[nums2_index]
                    nums_merged.append(num2)
                    nums2_index += 1
        
 
        
        is_characters_number_odd = len(nums_merged) % 2 == 1
        
        median_odd = nums_merged[len(nums_merged) // 2]
        median_even = (nums_merged[len(nums_merged) // 2] +  nums_merged[len(nums_merged) // 2 -1])/2
        
        median = median_odd if is_characters_number_odd else median_even
        
        print(nums_merged)
        print(is_characters_number_odd)  
        print(median_odd)
        print(median_even)
 

        return median