

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        originalMergedList = ListNode()
        
        mergedList = originalMergedList
        
        while list1 and list2:     
            mergedList.next = ListNode()
            mergedList = mergedList.next

            if list1.val < list2.val:
                mergedList.val = list1.val
                list1 = list1.next
            else:
                mergedList.val  = list2.val
                list2 = list2.next
                
        # At this point, either both lists are None or just one of them exist (and therefore has all the missing minimums)
        # So we can chain in in
        mergedList.next = list1 if list1 else list2
            
        return originalMergedList.next
            
        



# We can optimze the last case!
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        originalMergedList = ListNode()
        
        mergedList = originalMergedList
        
        while list1 or list2:
            
            mergedList.next = ListNode()
            mergedList = mergedList.next
            
            if not list1:
                mergedList.val = list2.val
                list2 = list2.next
            elif not list2:
                mergedList.val = list1.val
                list1 = list1.next
            else: # can be optimized!
                if list1.val < list2.val:
                    mergedList.val = list1.val
                    list1 = list1.next
                else:
                    mergedList.val  = list2.val
                    list2 = list2.next
            
            
        return originalMergedList.next
            
        