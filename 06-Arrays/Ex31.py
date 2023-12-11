array = [2,3,2,5,8,1,9,8]
x = []
if array[0] not in array[1:len(array)]:
    x.append(array[0])
if array[1] not in array[2:len(array)] and array[1] != array[0]:
    x.append(array[1])
for i in range(2,len(array)-1):
    if array[i] not in array[0:i] and array[i] not in array[i+1:len(array)]:
        x.append(array[i])

print(x)