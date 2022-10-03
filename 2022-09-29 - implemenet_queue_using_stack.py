#A Queue operates following the FIFO-Order
#An Stack using the LIFO

#We can use two stacks: stackIn and stackOut
#By popping elements from stackIn to stackOut,
# we’re able to reverse the ordering in such a way that the last elements of stackOut are always the first elements of stackIn.

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


#########################

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
