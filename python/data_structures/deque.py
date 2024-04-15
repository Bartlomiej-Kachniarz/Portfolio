class Queue:
    def __init__(self, max_len=10) -> None:
        self.running = True
        self.left = -1
        self.right = -1
        self.max_len: int = max_len
        self.deque: list = []
        self.main()

    def main(self) -> None:
        print("\n---- Main Menu ----")
        print("\n 1. Input restricted deque")
        print("\n 2. Output restricted deque")
        users_choice: str = input("\nEnter your choice: ")
        if users_choice == "1":
            self.input_deque()
        elif users_choice == "2":
            self.output_deque()
        else:
            print("Please enter either 1 or 2.")

    def input_deque(self) -> None:
        while self.running:
            print("===========================")
            print("\n\n INPUT RESTRICTED DEQUE")
            print("\n 1. Insert at right")
            print("\n 2. Delete from left")
            print("\n 3. Delete from right")
            print("\n 4. Display")
            print("\n Any other value to quit.")
            operation_choice = input("\n Enter your option: ")
            if operation_choice == "1":
                self.insert_right()
            elif operation_choice == "2":
                self.delete_left()
            elif operation_choice == "3":
                self.delete_right()
            elif operation_choice == "4":
                self.display()
            else:
                print("You have exited the input restricted deque.")
                self.running = False

    def output_deque(self) -> None:
        while self.running:
            print("===========================")
            print("\n\n OUTPUT RESTRICTED DEQUE")
            print("\n 1. Insert at right")
            print("\n 2. Insert at left")
            print("\n 3. Delete from left")
            print("\n 4. Display")
            print("\n Any other value to quit.")
            operation_choice = input("\n Enter your option: ")
            if operation_choice == "1":
                self.insert_right()
            elif operation_choice == "2":
                self.insert_left()
            elif operation_choice == "3":
                self.delete_left()
            elif operation_choice == "4":
                self.display()
            else:
                print("You have exited the output restricted queue.")
                self.running = False

    def insert_right(self) -> None:
        value_to_add: str = input("\n Enter your value to be added: ")
        if (self.left == 0 and self.right == self.max_len - 1) or (self.left == self.right + 1):
            print("OVERFLOW!")
            return
        if self.left == -1:  # empty queue initalization
            self.left = 0
            self.right = 0
        else:
            if self.right == self.max_len - 1:  # right is at last position of queue
                self.right = 0
            else:
                self.right += 1
        self.deque.append(value_to_add)

    def insert_left(self) -> None:
        value_to_add: str = input("\n Enter your value to be added: ")
        if (self.left == 0 and self.right == self.max_len - 1) or (self.left == self.right + 1):
            print("OVERFLOW!")
            return
        if self.left == -1:  # empty queue initalization
            self.left = 0
            self.right = 0
        else:
            if self.left == 0:  # left is at first position of queue
                self.left = self.max_len - 1
            else:
                self.left -= 1
        self.deque.insert(0, value_to_add)

    def delete_left(self) -> None:
        if self.left == -1:
            print("UNDERFLOW!")
            return
        print(f"The deleted element is {self.deque[0]}")
        self.deque.pop(0)
        if self.left == self.right:
            self.left = -1
            self.right = -1
        else:
            if self.left == self.max_len - 1:
                self.left = 0
            else:
                self.left += 1

    def delete_right(self) -> None:
        if self.left == -1:
            print("UNDERFLOW!")
            return
        print(f"The deleted element is {self.deque[self.right]}")
        self.deque.pop(self.right)
        if self.left == self.right:
            self.left = -1
            self.right = -1
        else:
            if self.right == 0:
                self.right = self.max_len - 1
            else:
                self.right -= 1

    def display(self) -> None:
        if self.left == -1:
            print("Queue is empty!")
            return
        print("\nThe elements of the queue are: ")
        print(self.deque)


if __name__ == "__main__":
    deque = Queue(max_len=11)
    deque.display()
