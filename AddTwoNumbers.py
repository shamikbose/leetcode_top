# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This function takes two numbers, represented as linked lists as inputs 
        and returns the result of their addition

        args:
        l1: First number represented as a list
        l2: Second number represented as a list

        return:
        Sum: Result of addition of l1 and l2, as a list
        """

        # Create an empty linked list to contain the result
        head = ListNode(0)
        pointer = head
        carry = 0
        while l1 is not None and l2 is not None:
            res = l1.val + l2.val + carry
            if res >= 10:
                pointer.next = ListNode(res - 10)
                carry = 1
            else:
                pointer.next = ListNode(res)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            pointer = pointer.next
        if l1 is None:
            while l2 is not None:
                res = l2.val + carry
                pointer.next = ListNode(res % 10)
                carry = res // 10
                l2 = l2.next
                pointer = pointer.next
        else:
            while l1 is not None:
                res = l1.val + carry
                pointer.next = ListNode(res % 10)
                carry = res // 10
                l1 = l1.next
                pointer = pointer.next
        if carry > 0:
            pointer.next = ListNode(carry)
        return head.next
