from merge_lists import Join, ListNode

# list1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# list2
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# merge the two lists
merged_list = Join().mergeTwoLists(list1, list2)

# print the single linked list
while merged_list:
    print(merged_list.value)
    merged_list = merged_list.next
print("None")