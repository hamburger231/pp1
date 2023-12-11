arr = [34,7,19,4,21,8]
x = 0
sum = 0
while x != len(arr):
    if arr[x]%2 == 0:
        sum += arr[x]
        x += 1
    else:
        x+= 1
print(sum)

