import math

from decorators import Counter, debug_this_func, do_twice, repeat, slow_down_by, slow_down_this_func, time_this_func


@time_this_func
@do_twice
def add_two_numbers(a, b):
    sum = a + b
    return f"Adding two numbers: {a} and {b} = {sum} \n"
    # return sum


@time_this_func
def sleepy_function(cycles):
    for _ in range(cycles):
        return sum([i for i in range(10000)])


@slow_down_by(sleep_time=2)
@debug_this_func
def introduce_yourself(name: str, age: int, nationality: str):
    if age >= 18:
        return f"{name} who is {nationality} is already an adult!"
    return f"{name} who is {nationality} is still a child."


math.factorial = debug_this_func(math.factorial)


def approximating_number_e(terms=7):
    sum = 0
    for n in range(terms):
        sum = sum + (1 / math.factorial(n))
    print(f"Calculated e = \n{sum}")
    print(f"Constant from math library = \n{math.e}")
    print(f"Error: {((math.e - sum) / math.e * 100):.10f}%")
    return sum


@slow_down_this_func
def factorial(number: int = 10):
    if number == 0:
        return 1
    return number * factorial(number - 1)


@repeat(num_times=5)
def logical_and(a=True, b=True):
    if a and b:
        print(True)
    else:
        print(False)


@repeat
@Counter
def logical_or(a=True, b=True):
    if a or b:
        print(True)
    else:
        print(False)


@Counter
def logical_xor(a=True, b=True):
    if a and b:
        print(False)
    elif not a and not b:
        print(False)
    else:
        print(True)


if __name__ == "__main__":
    add_two_numbers(4, 5)
    sleepy_function(1000)
    introduce_yourself("Adam", 29, "Polish")
    introduce_yourself("Zoe", 17, "French")
    approximating_number_e()
    print(f"Factorial of 10 is {factorial(10)}")
    logical_and(True, False)
    logical_or(False, True)
    logical_or(False, False)  # second call of the same function
    logical_xor(True, False)
    logical_xor(False, False)
