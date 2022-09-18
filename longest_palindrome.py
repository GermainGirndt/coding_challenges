class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        

        
        for i in range(len(s)):
            for j in range(len(s)):                
                print(j)
                for times in range(j + 1):
                    charPointerOneIndex = i+j+times
                    charPointerTwoIndex = len(s)-j-1+times
                    
                    
                    stringToCheck = s[charPointerOneIndex: charPointerTwoIndex]
                    print(f"i: {i}, j: {j}, times: {times}")
                    print(f"Index 1: {charPointerOneIndex}|| Index 2: {charPointerTwoIndex}")
                    print(stringToCheck)
                    if (self.checkForPalindrom(stringToCheck)):
                        return stringToCheck
                    
    
    
    def checkForPalindrom(self, s: str) -> bool:

        print()
        
        isOdd = len(s) % 2 == 1
        lastIndexToCheck = len(s) // 2 if isOdd else len(s) // 2 + 1

        print(f"String: {s}")
        for i in range(len(s)):

            firstChar = s[i]
            simetricLastChar = s[-i-1]
            print(f"First char: {s[i]} Simetric last char: {s[-i]}")
            
            if i == lastIndexToCheck:                
                if isOdd:
                    print("is odd")
                    print(f"Comparing: {firstChar}")
                    return True
                else:
                    print("is even")
                    print(f"Comparing: {firstChar} and {simetricLastChar}")
                    return firstChar == simetricLastChar

            print(f"Comparing: {firstChar} and {simetricLastChar}")
            if firstChar != simetricLastChar:
                print("no palindrom")
                return False


solution = Solution().longestPalindrome("abacaaad")
print("\nSolution: ")
print(solution)