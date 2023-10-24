import functools
import time


def do_twice(func):
    """Calling a function twice."""

    @functools.wraps(
        func
    )  # thanks to this decorator the wrapper_do_twice will pass all the information about the function "func"
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def time_this_func(func):
    """Print the time this function takes to run."""

    @functools.wraps(func)
    def wrapper_time_this_function(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        diff = end - start
        print(f"The {func.__name__!r} took {diff:.4f} seconds to complete. \n")
        return result

    return wrapper_time_this_function


def debug_this_func(func):
    """Print the functions signature and its returned values."""

    @functools.wraps(func)
    def wrapper_debug_this_function(*args, **kwargs):
        args_representation = [repr(arg) for arg in args]
        # kwargs_representation = [repr(kwarg) for kwarg in kwargs]
        kwargs_representation = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_representation + kwargs_representation)
        print(f"Calling: {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result!r}.\n")  # !r means that repr() is used
        return result

    return wrapper_debug_this_function


def slow_down_this_func(func):
    """Sleep half a second before calling this function."""

    @functools.wraps(func)
    def wrapper_slow_down_this_function(*args, **kwargs):
        time.sleep(0.5)
        return func(*args, **kwargs)

    return wrapper_slow_down_this_function


# Plug-in architecture example:
PLUGINS = dict()


def register(func):
    """Register a function as a plugin"""
    PLUGINS[func.__name__] = func
    return func


# A decorator that can take an argument but doesn't need to.
def repeat(_func=None, *, num_times=3):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_decorator_repeat(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper_decorator_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


# refactored slow_down_function
def slow_down_by(_func=None, *, sleep_time=1):
    """Sleep for the specified time before calling this function."""

    def decorator_slow_down_by(func):
        @functools.wraps(func)
        def wrapper_slow_down_by(*args, **kwargs):
            time.sleep(sleep_time)
            return func(*args, **kwargs)

        return wrapper_slow_down_by

    if _func is not None:
        return decorator_slow_down_by(_func)
    else:
        return decorator_slow_down_by


# Stateful decorator
def count_calls(func):
    """Count every call of the decorated function."""

    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Function: {func.__name__}. Call number: {wrapper_count_calls.num_calls}.")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


# Class as a decorator
class Counter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"Call number: {self.counter} of function {self.func.__name__}.")
        return self.func(*args, **kwargs)
