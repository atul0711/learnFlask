def beautiful_printer(func):
    def inner_func(*args, **kwargs):
        print("before execution")
        returned_value = func(*args, **kwargs)
        print("after execution")
        return returned_value.upper()
    return inner_func


@beautiful_printer
def calc(a):
    print("inside function")
    return a


print(calc("atul"))
