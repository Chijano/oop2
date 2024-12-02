from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper
