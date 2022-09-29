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
    
    
    def getLongestPalindromeForMiddleIndexes(self, string, left, right):
        palindrome = ""

        if left == right:
            palindrome = palindrome = string[left] + palindrome
            left -= 1
            right += 1

        while left >= 0 and right < len(string) and string[left] == string[right]:
            palindrome = string[left] + palindrome + string[right]
            left -= 1
            right += 1
        
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