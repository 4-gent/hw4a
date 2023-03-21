import time

def timestamp(func):
    current_time = time.ctime()
    print(current_time)
    return func()
@timestamp
def hi():
    print('hi')