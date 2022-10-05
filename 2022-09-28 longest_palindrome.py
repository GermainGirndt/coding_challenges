# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"




# The trick is to expand around the palindrome's center
# Due to it's nature, the palindromic center can have 1 or two letters.
# We have then to expand for this two cases
# There are 2n−1 such centers.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestPalindrome = ""
        for index in range(len(s)):
            # odd
            longestPalindromeForIndexes = self.getLongestPalindromeForMiddleIndexes(s, index, index)
            longestPalindrome = max(longestPalindrome, longestPalindromeForIndexes, key=len)
            
            # even
            longestPalindromeForIndexes = self.getLongestPalindromeForMiddleIndexes(s, index, index + 1)
            longestPalindrome = max(longestPalindrome, longestPalindromeForIndexes, key=len)
        
        return longestPalindrome
    
    
    def getLongestPalindromeForMiddleIndexes(self, string, leftIndex, rightIndex):
        palindrome = ""

        # first iteration of just one letter on the center
        if leftIndex == rightIndex:
            palindrome = string[leftIndex]
            leftIndex -= 1
            rightIndex += 1

        while leftIndex >= 0 and rightIndex < len(string) and string[leftIndex] == string[rightIndex]:
            palindrome = string[leftIndex] + palindrome + string[rightIndex]
            leftIndex -= 1
            rightIndex += 1
        
        return palindrome
            

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(len(s)):                
                for times in range(j + 1):
                    charPointerOneIndex = i+j+times
                    charPointerTwoIndex = len(s)-j-1+times
                    
                    
                    stringToCheck = s[charPointerOneIndex: charPointerTwoIndex]
                    if (self.checkForPalindrom(stringToCheck)):
                        return stringToCheck
                    
    
    
    def checkForPalindrom(self, s: str) -> bool:

        
        isOdd = len(s) % 2 == 1
        lastIndexToCheck = len(s) // 2 if isOdd else len(s) // 2 + 1

        for i in range(len(s)):

            firstChar = s[i]
            simetricLastChar = s[-i-1]
            
            if i == lastIndexToCheck:                
                if isOdd:
                    return True
                else:
                    return firstChar == simetricLastChar

            if firstChar != simetricLastChar:
                return False


solution = Solution().longestPalindrome("abacaaad")