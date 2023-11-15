def asteriksobeliks(n):
    for i in range(n):
        if i in range(n-1):
            print("*",end="/")
        else:
            print("*")
    
print(asteriksobeliks(4))