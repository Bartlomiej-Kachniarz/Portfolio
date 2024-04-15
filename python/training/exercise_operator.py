class ListManipulator:
    def __init__(self) -> None:
        self.calculation_list: list = []
        self.result = 0

    def execute(self, list_of_ops: list[str]) -> int:
        for operation in list_of_ops:
            try:
                self.result: int = self.result + int(operation)
                self.calculation_list.append(int(operation))
            except ValueError:
                pass

            if operation == "C":
                self.c_operation()
            elif operation == "D":
                self.d_operation()
            elif operation == "+":
                self.plus_operation()
        print(self.calculation_list)
        return self.result

    def c_operation(self) -> None:
        last_value = self.calculation_list.pop()
        self.result -= last_value

    def d_operation(self) -> None:
        last_value = self.calculation_list[-1] * 2
        self.calculation_list.append(last_value)
        self.result += last_value

    def plus_operation(self) -> None:
        value = self.calculation_list[-1] + self.calculation_list[-2]
        self.calculation_list.append(value)
        self.result += value


if __name__ == "__main__":
    operations = ListManipulator()
    result: int = operations.execute(list_of_ops=["5", "-2", "4", "C", "D", "9", "+", "+"])
    print(result)
