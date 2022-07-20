def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        arr = []
        i = 0
        # loop through linked list O(n)
        while curr:
            arr.append(curr.val)
            i += 1
            curr = curr.next
        curr = head
        i -= 1
        # another O(n)
        while curr:
            curr.val = arr[i]
            i -= 1
            curr = curr.next
        return head