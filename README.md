# merge-sorted-lists
#Given two linked lists, each representing a non-decreasingly sorted sequence of integers. 
# The task is to merge these two linked lists into a single, sorted linked list. The new list should be made by splicing together the nodes of the first two lists.
#Input:
# : the first linked list.
# list2: the second linked list.
# Each linked list node contains an integer value and a reference to the next node.
#Output:
# A single linked list that is the result of merging list1 and list2, sorted in non-decreasing order.
#Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.value <= 100
# list1 and list2 are sorted in non-decreasing order.
#Example:
#Input:
# list1 = 1 → 2 → 4
# list2 = 1 → 3 → 4
#Output: 1 → 1 → 2 → 3 → 4 → 4 → None