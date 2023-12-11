array = [[True,False],[True,True],[False,False]]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == True:
            array[i][j] = False
        else:
            array[i][j] = True
print(array)
    