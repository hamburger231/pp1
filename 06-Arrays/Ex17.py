array = [[0,0,0],
         [0,0,0],
         [0,0,0]]
x = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if j == i:
            array[i][x] = 1
            x += 1

    
        
            

print(array)


