
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        # On the output you can simply ignore the first node by calling next
        # That improves you writing cleaner code on the while loop
        output_root = ListNode()
        output = output_root
        
        carry = 0

        while(l1 or l2 or carry):
            
            partialResult = carry
            
            if (l1):
                partialResult += l1.val
                l1 = l1.next
                
            
            if (l2):
                partialResult += l2.val
                l2 = l2.next

            # Instead of verifying if the partial result is greather than 10 for calculating the carry,
            # it's cleaner to just to that immediately
            carry = partialResult // 10
            partialResult = partialResult % 10            
           
            output.next = ListNode()
            output = output.next
            output.val = partialResult
            
          
        return output_root.next


### Before
class InitialSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        
        output_root = ListNode()
        output = output_root
        while(True):
            
            partialResult = 0
            
            if (l1):
                partialResult += l1.val
                print(l1.val)
                l1 = l1.next
                
            
            if (l2):
                partialResult += l2.val
                print(l2.val)
                l2 = l2.next

                
            partialResult += carry
            carry = 0
  
            
            if partialResult >= 10:
               partialResult = partialResult % 10
               carry += 1
            
            output.val = partialResult

            if (l1 is None and l2 is None and carry == 0):
                return output_root
            
            output.next = ListNode()
            output = output.next
            
            