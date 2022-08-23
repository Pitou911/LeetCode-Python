class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        cur1 = l1
        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next
        s1, s2 = s1[::-1], s2[::-1]
        res = int(s1) + int(s2)
        dummy = ListNode(0)
        p = dummy
        if res == 0:
            return dummy
        while res > 0:
            temp = ListNode(res%10)
            res = res//10
        
# class Solution(object):    
    #second method
    # def addTwoNumbers(self, l1, l2):
    #     carry = 0
    #     ls = ListNode()
    #     curr = ls
    #     while l1 or l2 or carry:
    #         v1 = l1.val if l1 else 0
    #         v2 = l2.val if l2 else 0
            
    #         # new digit
    #         val = v1 + v2 + carry
    #         carry = val // 10
    #         val = val % 10
    #         curr.next = ListNode(val)
            
    #         #update pointer
    #         curr = curr.next
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return ls.next