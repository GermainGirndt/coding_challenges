class MyQueue(object):
    
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackIn.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.stackOut:
            self.reverseInOutOrder()

        return self.stackOut.pop()


    def peek(self):
        """
        :rtype: int
        """

        if not self.stackOut:
            self.reverseInOutOrder()
            
        return self.stackOut[-1]
    
    def reverseInOutOrder(self):
        for _ in range(len(self.stackIn)):
                last = self.popLast(self.stackIn)
                self.stackOut.append(last)
        

    def empty(self):
        """
        :rtype: bool
        """

        return not self.stackIn and not self.stackOut

    def getLastIndex(self, stack):
        return len(stack) - 1

    def popLast(self, stack):
        return stack.pop(self.getLastIndex(stack))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

##########
class MyQueueTwo(object):

    stackOne = None
    stackTwo = None
    
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackOne.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        
        for i in range(len(self.stackOne)):
            last = self.stackOne.pop(self.getLastIndex(self.stackOne))
            self.stackTwo.append(last)
        
        queueFirst = self.stackTwo.pop(self.getLastIndex(self.stackTwo))

        for i in range(len(self.stackTwo)):
            last = self.stackTwo.pop(self.getLastIndex(self.stackTwo))
            self.stackOne.append(last)

        return queueFirst


    def peek(self):
        """
        :rtype: int
        """
        
        for i in range(len(self.stackOne)):
            last = self.stackOne.pop(self.getLastIndex(self.stackOne))
            self.stackTwo.append(last)
        
        queueFirst = self.stackTwo.pop(self.getLastIndex(self.stackTwo))
        self.stackOne.append(queueFirst)

        for i in range(len(self.stackTwo)):
            last = self.stackTwo.pop(self.getLastIndex(self.stackTwo))
            self.stackOne.append(last)

        return queueFirst
        
        
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.stackOne) == 0
    
    def getLastIndex(self, stack):
        return len(stack) - 1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()