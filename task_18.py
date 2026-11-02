import functools
import datetime

def log_calls(file_name):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*argument):
            time = datetime.datetime.now()
            with open (file_name,"a") as f:
                f.write(f"{time}: {function.__name__} {argument}\n")
            return function(*argument)
        return wrapper
    return decorator

@log_calls("log.calls")
def sum(a, b):
    return a + b

print(sum(4, 5))   