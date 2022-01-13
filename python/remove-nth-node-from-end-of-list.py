# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        delete = head
        node = head
        prev = None
        k = 1
        while True:
            if node == None:
                if prev == None:
                    return head.next
                prev.next = delete.next
                return head
            if k > n:
                prev = delete
                delete = delete.next
            k += 1
            node = node.next
            