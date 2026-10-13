# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        prev = None 
        mover = head 

        while mover:
            temp = mover.next 

            mover.next =  prev

            prev = mover 
            mover = temp

        return prev