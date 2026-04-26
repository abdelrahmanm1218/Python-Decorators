import stat
import time


def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

# @my_decorator
# def hello():
#     print("Hello, World!")




def calc_runtime(func):
    def wrapper(*args, **kwargs):
        print("Start decorator")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time execution: {end_time - start_time} Secs.")
        print("end decorator")
        return result 
    return wrapper


# @calc_runtime
# def delay_by(t):
#     time.sleep(t)
#     print("testing test func")
#     time.sleep(1)
#     print("Ended test function")
#     return "finished delay function"

# print(delay_by(t=4))