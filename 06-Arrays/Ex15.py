array = [[1,3,5],[8,7,2]]
x = 0
print(array[0][0]+array[1][-1])
print(array[0][len(array[0])//2]+array[1][len(array[1])//2])
for i in range(len(array[1])):
    x += array[1][i]
print(x)

