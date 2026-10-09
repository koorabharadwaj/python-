class Node:
    
    def __init__(self, data):
        self.data = data  # Stores the actual data
        self.next = None  # Pointer to the next node, defaults to None

class LinkedList:
    """Represents the linked list structure."""
    def __init__(self):
        self.head = None  # Points to the first node in the list

    def prepend(self, data):
        """Inserts a new node at the beginning of the list. Time Complexity: O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Inserts a new node at the end of the list. Time Complexity: O(n)"""
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Link the last node to the new node
        current.next = new_node

    def delete(self, key):
        """Deletes the first node that contains the specified data value. Time Complexity: O(n)"""
        current = self.head

        # Case 1: The list is empty
        if not current:
            print("List is empty.")
            return

        # Case 2: The node to delete is the head node
        if current.data == key:
            self.head = current.next
            current = None
            return

        # Case 3: Search for the node to delete, keeping track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found in the list
        if not current:
            print(f"Value '{key}' not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def display(self):
        """Traverses and prints the linked list elements."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


# --- Example Usage ---
if __name__ == "__main__":
    # Initialize the linked list
    llist = LinkedList()

    # Append elements
    llist.append(10)
    llist.append(20)
    llist.append(30)
    print("Initial List:")
    llist.display()  # Output: 10 -> 20 -> 30 -> None

    # Prepend an element
    llist.prepend(5)
    print("\nAfter prepending 5:")
    llist.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

    # Delete an element from the middle
    llist.delete(20)
    print("\nAfter deleting 20:")
    llist.display()  # Output: 5 -> 10 -> 30 -> None

    # Delete the head element
    llist.delete(5)
    print("\nAfter deleting head (5):")
    llist.display()  # Output: 10 -> 30 -> None
