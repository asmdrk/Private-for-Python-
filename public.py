from priv import privatize

@privatize
def add(x, y):
    print("executing function!")

print(add(5, 7))