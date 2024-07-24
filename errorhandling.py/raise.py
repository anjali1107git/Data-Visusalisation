def checkage(age):
    try:
       if age>=18:
        print("you are eligible for do anything")
       else:
        raise  ValueError
    except ValueError:
       print("the age is not valid")
    
    
    
checkage(16)
checkage(19)