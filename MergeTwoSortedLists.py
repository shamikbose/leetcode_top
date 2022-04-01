# Difficulty: Easy
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        While l1 and l2 have values not checked, check the first element in each list
            if element in l1 is larger, insert element from l2 into new list
            else insert element from l1 into new list
        Enter elements from list that's not completely checked into new list in order

        args:
        l1, l2: lists of numbers in sorted order

        return:
        head of new list 
        """
        temphead = ListNode()
        newList = temphead
        while l1 and l2:
            if l1.val > l2.val:
                temphead.next = ListNode(l2.val)
                l2 = l2.next
            else:
                temphead.next = ListNode(l1.val)
                l1 = l1.next
            temphead = temphead.next
        if l1:
            temphead.next = l1
        elif l2:
            temphead.next = l2
        return newList.next

