import functools

def type_check(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if not isinstance(args[i], expected_types[i]):
                    raise TypeError("Неверный тип")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def sum(a, b):
    return a + b

print(sum("4", 5))
