# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = head
        if not prev:
            return head
        curr = prev.next
        while curr:
            if curr.val != prev.val:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                del curr
                curr = prev.next
        return head