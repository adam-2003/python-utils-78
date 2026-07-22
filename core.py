import time
import functools


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"{func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def complex_calculation(n):
    total = 0
    for i in range(n):
        total += (i ** 2)
    return total


@timing_decorator
def another_heavy_task(n):
    return sum(i * 2 for i in range(n))


if __name__ == "__main__":
    print(complex_calculation(1000000))
    print(another_heavy_task(1000000))