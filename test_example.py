def sum(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        return x/y
    except ValueError:
        print("Error in division")

x, y = 1, 2
print(divide(x,y))
