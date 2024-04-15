from collections import deque
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self, item) -> None:
        self.items.popleft()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)

    def show_dict(self) -> None:
        return print(self.__dict__)


if __name__ == "__main__":
    queue1 = Queue()
    print(queue1)
    print(queue1.is_empty())
    queue1.enqueue(item="Q")
    queue1.enqueue(item="U")
    queue1.enqueue(item="I")
    queue1.enqueue(item="Z")
    print(queue1)
    queue1.dequeue(item="Q")
    print(queue1)
    queue1.show_dict()
    queue2 = Queue()
    print(queue1)
    print(queue2.is_empty())
    queue2.enqueue(item="D")
    queue2.enqueue(item="E")
    queue2.enqueue(item="F")
    print(queue2)
    queue2.dequeue(item="E")
    queue2.show_dict()
