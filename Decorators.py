from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper


def standard_format(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return f"Standard Report:\n{data}"
    return wrapper


def tax_authority_format(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return f"Tax Authority Report:\nHeader: Tax Info\n{data}\nFooter: End of Tax Info"
    return wrapper


def securities_agency_format(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return f"Securities Agency Report:\nSTART--{data}--END"
    return wrapper
