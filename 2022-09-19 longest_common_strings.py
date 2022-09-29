

# "if not list" for readability
# we can use the shortest string as base to compare with the others
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longestCommonString = ""
        
        if not strs:
            return longestCommonString
        
        shortestString = min(strs, key=len)
        
        
        for index, char in enumerate(shortestString):            
            for string in strs:
                if (string[index] != char):
                    return longestCommonString
            longestCommonString += char
        
        return longestCommonString
            
             
            
        


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longestCommonString = ""
        
        if len(strs) == 0:
            return longestCommonString
        
        minCharCount = len(strs[0])
        for string in strs:
            minCharCount = min(minCharCount, len(string))
        
        for index in range(minCharCount):
            actualComparingChar = strs[0][index]
            
            for string in strs:
                if (string[index] != actualComparingChar):
                    return longestCommonString
            longestCommonString += actualComparingChar
        
        return longestCommonString
            
             
            
        