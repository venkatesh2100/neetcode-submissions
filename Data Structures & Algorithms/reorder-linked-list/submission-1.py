# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow = head 
        fast = head 

        while fast and fast.next:

            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None 

        first = head
        # reverse the seond 
        prev = None
        while second:
            temp = second.next 

            second.next = prev 
            prev = second 
            second = temp 

        second = prev 

        #merge (first and secnod) 

        head = ListNode()
        curr = head 
        check = True
        while first and second:

            if check:
                curr.next = first
                first = first.next 
            else:
                curr.next = second 
                second = second.next 
            curr = curr.next 
            check = not check

        if first:
            curr.next = first
        if second:
            curr.next = second

    

            
