def checkage(age):
       if age>=18:
        print("you are eligible for do anything")
       else:
        raise  ValueError("your age is less than 18")
try:
    checkage(15)
except ValueError as V:
    print("something went wrong",V)