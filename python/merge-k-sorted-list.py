"""
div and conquer:

div list into pairs
merge them recursviely
"""


def merge(x, y):
    head = ListNode()
    node = head

    while True:
        if x == None:
            node.next = y
            break
        if y == None:
            node.next = x
            break
        if x.val > y.val:
            node.next = ListNode(y.val)
            node = node.next
            y = y.next
        else:
            node.next = ListNode(x.val)
            node = node.next
            x = x.next
    return head.next


def divcon(lists):
    n = len(lists)
    if n == 0:
        return None
    if n == 1:
        return lists[0]
    l1 = divcon(lists[:n//2])
    l2 = divcon(lists)[n//2:]
    return merge(l1, l2)