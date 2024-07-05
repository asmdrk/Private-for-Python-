import inspect
def privatize(fun):
    def wrapper(*args, **kwargs):
        # print(inspect.getmembers(fun))
        frame = inspect.stack()
        first = frame[0]
        last = frame[-1]
        if (first.filename != last.filename):
            print("hey dont call that! lol")
        else: 
            fun(*args, **kwargs)
        # inspect the caller of the function, or the path to the caller, if its not filepath say no?? ig
        #if everything is fine call the function
         
    return wrapper
@privatize
def add(x,y):
    print("executing function!")

print(add(5,7))