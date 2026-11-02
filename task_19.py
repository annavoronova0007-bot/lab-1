import functools
import datetime
results = {}

def cache(function):
    @functools.wraps(function)
    def wrapper(*argument):
        key = argument
        if key not in results:
            results[key] = function(*argument)
            print(f"[cache-write] {function.__name__}{argument}")
        else:
            print(f"[cache-hit] {function.__name__}{argument}")
        return results[key]
    
    return wrapper
@cache
def sum(a, b):
    return a + b

sum(4, 5)