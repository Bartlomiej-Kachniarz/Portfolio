class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.is_empty())
    stack.push(5)
    print(stack)
    stack.push(23)
    stack.push(0)
    stack.push(12)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.size())
