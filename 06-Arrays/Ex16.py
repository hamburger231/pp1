array = [
    [3,9,2],
    [2,4,5],
    [7,1,6],
    [0,4,8]
    ]
x = 0
for i in array:
    for j in i:
        if j%2 != 0:
            x += 1

print(x)