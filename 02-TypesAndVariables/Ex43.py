x = str(input("Name: "))
a = len(x)
for i in range(a):
    print(x[i],"(",ord(x[i]),")",sep="",end=" ")