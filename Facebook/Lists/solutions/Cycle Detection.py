

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    visited_nodes = set()
    current_node = head
    while current_node.next is not None:
        if current_node.next in visited_nodes:
            return 1
        else:
            visited_nodes.add(current_node.next)
            current_node = current_node.next
    return 0

