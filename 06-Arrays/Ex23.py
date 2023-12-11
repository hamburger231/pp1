array = [-15, 8, -31, 47, -2, 19]
x = []
max = (-999999999999999999999999999999999999999)
min = (10000000000000000000000000000000000000000000000000000)
for i in range(len(array)):
    for j in array:
        if array[i] > max:
            max = array[i]
        if array[i] < min:
            min = array[i]
print(max)
print(min)