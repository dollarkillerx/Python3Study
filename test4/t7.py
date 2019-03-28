import time

def decorator(func) :
    def wrapper(*args) :
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(fun_name) :
    print('This is a function ' + fun_name)

@decorator
def f2(func_name,funcname2) :
    print('This is a function ' + func_name + funcname2)


f1('dollarkiller')

f2('dollarsda','asdasdsad')