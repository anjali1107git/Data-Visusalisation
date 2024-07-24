try:
    num=int(input("Enter the number:"))
    print("The number is:",num) 
except ValueError:
    print("Input is not a valid Integer")