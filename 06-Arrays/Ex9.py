burger = [2,3,7,5,4]
print(burger)
print(len(burger))
print(burger[0])
print(burger[1])
print(burger[-1])
print(burger[len(burger)-2])
print(burger[0]+burger[-1])
print(burger[len(burger)//2])

for i in range(len(burger)):
    print(burger[i], end=" ")
