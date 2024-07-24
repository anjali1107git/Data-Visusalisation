try:
    f=open("abc.txt")
except FileNotFoundError:
    print("File not found")