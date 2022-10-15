"""Decorators can access and modify:
    input args, return values, raised exceptions.

"""
from functools import wraps

def trace(func):
    # copies all of the imp metadata abt the inner func to the outer func
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling : {func.__name__}({args!r}, {kwargs!r}) ')
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))


if __name__ == '__main__':
    fibonacci(4)