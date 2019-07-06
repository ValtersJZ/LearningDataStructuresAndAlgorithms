class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        """Append a node to the end of the LinkedList"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_position(self, position):
        """Return the node at the given position.
        None if position is invalid"""
        current = self.head
        current_pos = 1

        if position < 1:
            return None
        while current_pos <= position and current is not None:
            if current_pos == position:
                return current
            current = current.next
            current_pos += 1
        return None

    def insert(self, new_node, position):
        current = self.head
        current_pos = 1

        if position > 1:
            while current_pos <= position:
                if current_pos == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                current_pos += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        current = self.head
        previous = None
        if current:
            while current.value != value and current.next:
                previous = current
                current = current.next
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next


if __name__ == "__main__":
    # Simple visual tests
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # print 3
    print(ll.head.next.next.value)
    # print 3
    print(ll.get_position(3).value)

    ll.insert(e4, 3)
    # print 4
    print(ll.get_position(3).value)

    ll.delete(1)
    # print 2
    print(ll.get_position(1).value)
    # print 4
    print(ll.get_position(2).value)
    # print 3
    print(ll.get_position(3).value)
