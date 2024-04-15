from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return not self.items

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> None:
        self.items.pop()

    def peek(self) -> Any:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.is_empty())
    stack.push(item=5)
    print(stack)
    stack.push(item=23)
    stack.push(item=0)
    stack.push(item=12)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.size())
