import time
import functools

def timing(function):
    @functools.wraps(function)
    def wrapper(*argument):
        start_time = time.perf_counter()
        result = function(*argument)
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        
        print("Время выполнения:", round(execution_time_ms, 4), "мс")
        
        return result
    return wrapper

@timing
def sum(a, b):
    return a + b

print("Результат:", sum(4, 5)) 