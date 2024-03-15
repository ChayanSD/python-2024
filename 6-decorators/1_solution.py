import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} function ran in {end - start} time")
        return result
    return wrapper


@timer
def execute_func(n):
    time.sleep(n)


execute_func(2)