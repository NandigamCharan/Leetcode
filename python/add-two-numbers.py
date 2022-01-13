# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        prev = ListNode()
        prev.next = l1
        c = 0
        while True:
            if n1 == None and n2 == None and c == 0:
                break
            if prev.next == None:
                prev.next = ListNode()
                n1 = prev.next
            x = 0 + n1.val + c if n2 == None else n2.val + n1.val + c
            c = x // 10
            n1.val = x % 10
            n1 = n1.next
            if n2:
                n2 = n2.next
            prev = prev.next
        return l1