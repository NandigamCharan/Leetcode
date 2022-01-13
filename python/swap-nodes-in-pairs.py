# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        x.next = head
        node = x
        while True:
            if node.next == None or node.next.next == None:
                break
            t = node.next
            node.next = node.next.next
            temp = node.next.next
            node.next.next = t
            t.next = temp
            node = node.next.next
        return x.next
