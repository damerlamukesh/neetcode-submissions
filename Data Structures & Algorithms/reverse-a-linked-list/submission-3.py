# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # optimal is chasnging the addresses of the Lunked list TC=O(n), SC=O(1)
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            
        return prev

        
        
        
        