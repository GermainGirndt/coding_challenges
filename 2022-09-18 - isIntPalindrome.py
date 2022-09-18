### We don't need to revert the whole number
### Insted we could aproximate it to the half
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x == 0:
            return True
        
        if x < 0:
            return False
        
        if x % 10 == 0:
            return False
                

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
            
        return x == revertedNumber or x == revertedNumber // 10
            

            
            
        



### Works, but uses always n operations for reverting the number
### Can we do it better?
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        if x == 0:
            return True
        
        if x < 0:
            return False

        copyX = x
        
        revertedNumber = 0
        while copyX != 0:
            revertedNumber = revertedNumber * 10 + copyX % 10
            copyX = copyX // 10
            
        return x == revertedNumber 