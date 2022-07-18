class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
  
  
# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None
  
    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
  
    # Method to add element to list
    def addToList(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
  
        last = self.head
        while last.next:
            last = last.next
  
        last.next = newNode
def mergeTwoLists(list1, list2):
        result = ListNode(None)
        temp = result
        while True:
            if list1 is None:
                temp.next = list2
                break
            if list2 is None:
                temp.next = list1
                break
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        return result.next

listA = LinkedList()
listB = LinkedList()
listA.addToList(1)
listA.addToList(3)
listA.addToList(6)
listA.addToList(7)
listB.addToList(1)
listB.addToList(2)
listB.addToList(3)
listB.addToList(8)
listC = LinkedList()
listC.head = mergeTwoLists(listA.head, listB.head)
listC.printList()