import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


def insertion_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_head = insert_node_sorted(sorted_head, current)
        current = next_node

    return sorted_head


def insert_node_sorted(head, new_node):
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


def reverse_linked_list(linked_list):
    current = linked_list.head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev
    return linked_list


def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()

    current1 = list1
    current2 = list2

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def initialize_list(linked_list):
    for _ in range(10):
        linked_list.append(random.randint(1, 50))
    return linked_list


# initialize lists
linked_list1 = LinkedList()
linked_list1 = initialize_list(linked_list1)

linked_list2 = LinkedList()
linked_list2 = initialize_list(linked_list2)

linked_list3 = LinkedList()
linked_list3 = initialize_list(linked_list3)

# print results
print("\nReverse a linked list by changing node references")
print("Initial list:")
linked_list3.display()
print("Reversed list:")
reversed_list = reverse_linked_list(linked_list3)
reversed_list.display()

print("\nSort a linked list using insertion sort")
print("Initial list:")
linked_list1.display()
print("Sorted list:")
sorted_head = insertion_sort_linked_list(linked_list1.head)
print_linked_list(sorted_head)

print("\nMerge two sorted linked lists into one sorted list")
print("List 1:")
print_linked_list(sorted_head)
sorted_head2 = insertion_sort_linked_list(linked_list2.head)
print("List 2:")
print_linked_list(sorted_head2)
print("Merged list:")
merged_list = merge_sorted_lists(sorted_head, sorted_head2)
merged_list.display()
