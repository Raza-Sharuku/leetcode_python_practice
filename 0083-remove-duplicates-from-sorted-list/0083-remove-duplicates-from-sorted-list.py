# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        start = head
        while (start and start.next):
            if (start.val == start.next.val):
                start.next = start.next.next
                continue
            start = start.next
        return (head)
        