import random

from decorators import PLUGINS, register


@register
def hello_world(name):
    print(f"Hello World! I am {name}!")


@register
def who_are_you(name):
    print(f"I am {name}. Who are you?")


@register
def where_is(name):
    print(f"Do you know where is {name}?")


def random_registered_func(name):
    func_name, func = random.choice(list(PLUGINS.items()))
    print(f"Using {func_name!r}")

    return func(name)


if __name__ == "__main__":
    random_registered_func("Bart")
