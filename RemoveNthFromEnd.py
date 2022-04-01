#Difficulty: Medium
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 2-pass solution
        # Count number of nodes in first pass
        # Remove (size-n)th node
        temp = head
        count = 0
        while head:
            count += 1
            head = head.next
        head = temp
        if count == 1:
            return None
        if count == n:
            return head.next
        while head:
            if count == n + 1:
                if head.next:
                    head.next = head.next.next
                else:
                    head.next = None
                break
            else:
                head = head.next
            count -= 1
        return temp
