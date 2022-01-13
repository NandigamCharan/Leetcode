# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(head):
            slow = head
            fast = head
            while True:
                if fast.next == None:
                    return slow
                if fast.next.next == None:
                    return slow.next
                fast = fast.next.next
                slow = slow.next
        return recurse(head)