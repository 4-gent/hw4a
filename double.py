def double(func):
    func()
    print('Let\'s try that again!')
    return func
@double
def greet():
    print('Hello world!')
greet()