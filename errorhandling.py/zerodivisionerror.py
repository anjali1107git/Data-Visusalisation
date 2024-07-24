a=int(input("Enter the number:"))
b=int(input("Enter the division:"))
try:
    a/b
except ZeroDivisionError as e:
    print(e)
    