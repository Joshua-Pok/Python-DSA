class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        end = len(self.items) + 1
        return self.items[end]

    def pop(self):
        if len(self.items) < 1:
            return

        return self.items.pop()
