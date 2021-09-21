
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.size = 0

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return self.head
        else:
            return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        return self.size

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if (self.size + 1) < index:
            return None

        counter = 0
        current = self.head
        while current:
            if counter == index:
                return current.value
            current = current.next
            counter += 1

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None

        current = self.head

        while current.next:
            current = current.next
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.size == 0:
            self.add_first(value)
        else:
            new_node = Node(value)
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None

        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.size == 0:
            return None

        current = self.head
        if current.value == value:
            self.head = current.next

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next
        self.size -= 1

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next

        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverse(self):
        if self.size == 0:
            return None

        previous = None
        current = self.head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        middle_index = (self.size // 2)
        return self.get_at_index(middle_index)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        index = (self.size - n) - 1
        return self.get_at_index(index)

    # returns the node at a given index, rather than the value
    def get_node_at_index(self, index):
        if (self.size + 1) < index:
            return None

        counter = 0
        current = self.head
        while current:
            if counter == index:
                return current
            current = current.next
            counter += 1

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def has_cycle(self):
        if self.size == 0:
            return False

        current = self.head

        for i in range(0, self.size):
            current = self.get_node_at_index(i)
            if current.next == self.head:
                return True
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
