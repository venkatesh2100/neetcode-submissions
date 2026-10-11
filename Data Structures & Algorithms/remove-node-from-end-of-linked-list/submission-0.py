# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        curr = head
        i = 0
        N = 0 
        while curr:
            N+=1
            curr = curr.next 
        curr = head
        # prev = None 
        if (N-n) == 0:
            return head.next

        while curr and curr.next:

            if i == (N-n-1):
                curr.next = curr.next.next 
                break

            curr = curr.next 
            i+=1
        return head
