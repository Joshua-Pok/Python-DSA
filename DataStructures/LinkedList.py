class Node:
    def __init__ (self, val):
        self.head = None

    def __iter__(self):
        """Generator Function that yields each node from head to tail"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

            
