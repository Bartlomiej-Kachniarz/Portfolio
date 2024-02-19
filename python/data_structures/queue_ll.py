from collections import deque


class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self, item):
        self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)

    def show_dict(self):
        return print(self.__dict__)


if __name__ == "__main__":
    queue1 = Queue()
    print(queue1)
    print(queue1.is_empty())
    queue1.enqueue("Q")
    queue1.enqueue("U")
    queue1.enqueue("I")
    queue1.enqueue("Z")
    print(queue1)
    queue1.dequeue("Q")
    print(queue1)
    queue1.show_dict()
    queue2 = Queue()
    print(queue1)
    print(queue2.is_empty())
    queue2.enqueue("D")
    queue2.enqueue("E")
    queue2.enqueue("F")
    print(queue2)
    queue2.dequeue("E")
    queue2.show_dict()
