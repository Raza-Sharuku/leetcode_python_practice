# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_result = 0
        demi = 1
        if (l1.next == None):
            l1_result = l1.val
        else:
            while l1 != None:
                l1_result = l1_result + l1.val * demi
                demi *= 10
                l1 = l1.next
        l2_result = 0
        demi = 1
        if (l2.next == None):
            l2_result = l2.val
        else:
            while l2 != None:
                l2_result = l2_result + l2.val * demi
                demi *= 10
                l2 = l2.next
        
        result = l1_result + l2_result
        l3 = ListNode()
        head = l3
        while (result > 0):
            l3.val = result % 10
            result = result / 10
            if (result > 0):
                l3.next = ListNode()
                l3 = l3.next
        return (head)


        