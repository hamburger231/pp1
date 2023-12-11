import random
array = [random.randint(1,999) for i in range(8)]

print("-"*50)
print("|  ",end="")
for i in array:
    print(i,end="|  ")
print("")
print("-"*50)