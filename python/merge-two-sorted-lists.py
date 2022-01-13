# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        while True:
            if l1 == None:
                tail.next = l2
                break
            if l2 == None:
                tail.next = l1
                break
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail.next.next = None
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail.next.next = None
                tail = tail.next
        return head.next