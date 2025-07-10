def divide(a,b):
    try:
        res=a/b
        return a / b
    except ZeroDivisionError:
        print("division by zero is not allowed")
print(divide(10,0))