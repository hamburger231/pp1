a = int(input("Provide A: "))
b = int(input("Provide B: "))

for i in range(0,a):
    print("*", end="")
print("")
for i in range (2,b):
    print("*"," "*(a-4),"*")
for i in range(0,a):
    print("*", end="")

