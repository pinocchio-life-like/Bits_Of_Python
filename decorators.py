def decorator(func):
    def wrapper_func():
        print("##########")
        func()
        print("##########")
    return wrapper_func

@decorator
def hello_func():
    print("Helllooooo")
    

hello_func()
