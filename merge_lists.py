class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Join:
    def mergeTwoLists(self, l1, l2):
        head = placeholder =  ListNode(0)

        while l1 and l2:
            if l1.value < l2.value:
                placeholder.next = l1
                l1 = l1.next
            else:
                placeholder.next = l2
                l2 = l2.next
            placeholder = placeholder.next

        placeholder.next = l1 or l2

        return head.next